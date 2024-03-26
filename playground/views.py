# users/views.py
import json
import random
import time
import uuid
from django.http import JsonResponse
from faker import Faker
from django.utils import timezone
from .models import Appointment, CustomUser, Entity, MedicalEntityManager, MedicalPatient, MedicalProfessional, MedicalUser, Address, Person, RandomWriteObject, UnencryptedAddress, UnencryptedAppointment, UnencryptedEntity, UnencryptedMedicalUser, UserLogin
from django.db.models import Count
from .serializers import MedicalUserSerializer, UnencryptedMedicalUserSerializer, UserLoginSerializer

def generate_users(request):
    fake = Faker()
    # Generate 100 addresses
    for i in range(1000):
        # Generate fake data
        address_line_1 = fake.street_address()
        address_line_2 = fake.street_address()
        city = fake.city()
        post_code = fake.postcode()

        # Create Address object
        address = Address.objects.create(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            post_code=post_code,
        )

        # Generate fake data
        encryptedName = fake.user_name()
        username = fake.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        ethnicity = ['White', 'Black', 'Asian', 'Hispanic', 'Other'][random.randint(0, 4)]
        birthdate = fake.date_of_birth()

        # Create MedicalUser object
        user = MedicalUser.objects.create_user(
            encryptedName = encryptedName,
            username = str(i) + username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            ethnicity =  ethnicity,
            birthdate = birthdate,
            address = address
        )
    return JsonResponse({'message': 'User generation completed'})


def generate_unencrypted_users(request):
    fake = Faker()
    # Generate 100 addresses
    for i in range(1000):
        # Generate fake data
        address_line_1 = fake.street_address()
        address_line_2 = fake.street_address()
        city = fake.city()
        post_code = fake.postcode()

        # Create Address object
        address = UnencryptedAddress.objects.create(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            post_code=post_code,
        )

        # Generate fake data
        encryptedName = fake.user_name()
        username = fake.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        ethnicity = ['White', 'Black', 'Asian', 'Hispanic', 'Other'][random.randint(0, 4)]
        birthdate = fake.date_of_birth()

        # Create MedicalUser object
        user = UnencryptedMedicalUser.objects.create_user(
            encryptedName = encryptedName,
            username = str(i) + username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            ethnicity =  ethnicity,
            birthdate = birthdate,
            address = address
        )
    return JsonResponse({'message': 'Unencrypted user generation completed'})

def view_users(request):
    # get all users and convert to json to return
    users = MedicalUser.objects.all.values()
    json_data = json.dumps(list(users))
    return JsonResponse({"message": "Found all these users: ", "users": json_data})


def delete_users(request):
    # delete all users
    MedicalUser.objects.all().delete()
    Address.objects.all().delete()
    UnencryptedMedicalUser.objects.all().delete()
    UnencryptedAddress.objects.all().delete()
    Entity.objects.all().delete()
    UnencryptedEntity.objects.all().delete()

    return JsonResponse({'message': 'All users and addresses deleted'})   

def get_users(request, limit=-1):
    if limit == -1:
        medical_users = MedicalUser.objects.all()
    else:
        medical_users = MedicalUser.objects.all()[:limit]
    serializer = MedicalUserSerializer(medical_users, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_unencrypted_users(request, limit=-1):
    if limit == -1:
        medical_users = UnencryptedMedicalUser.objects.all()
    else:
        medical_users = UnencryptedMedicalUser.objects.all()[:limit]
    serializer = UnencryptedMedicalUserSerializer(medical_users, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_usernames(request, limit=-1):
    if limit == -1:
        # get only the usernames of all users, without .all()
        medical_users = MedicalUser.objects.values_list('encryptedName')
    else:
        medical_users = MedicalUser.objects.values_list('encryptedName')[:limit]
    return JsonResponse(list(medical_users), safe=False)

def get_ethnicities(request, limit=-1):
    if limit == -1:
        # get only the ethnicities of all users, without .all()
        medical_users = MedicalUser.objects.values_list('ethnicity')
    else:
        medical_users = MedicalUser.objects.values_list('ethnicity')[:limit]
    return JsonResponse(list(medical_users), safe=False)

def delete_data(request):
    RandomWriteObject.objects.all().delete()
    return JsonResponse({'message': 'All objects deleted'})   

def generate_appointment_data(request, limit = 100):
    fake = Faker()
    # Generate 100 objects

    # Generate fake data
    address_line_1 = fake.street_address()
    address_line_2 = fake.street_address()
    city = fake.city()
    post_code = fake.postcode()
    # Create Address object
    address = Address.objects.create(
        address_line_1=address_line_1,
        address_line_2=address_line_2,
        city=city,
        post_code=post_code,
    )
    unencryptedAddress = UnencryptedAddress.objects.create(
        address_line_1=address_line_1,
        address_line_2=address_line_2,
        city=city,
        post_code=post_code,
    )

    entityName = fake.word()
    # generate 5 entities

    entity = Entity.objects.create(
        name = entityName,
        address = address
    )
    unencryptedEntity = UnencryptedEntity.objects.create(
        name = entityName,
        address = unencryptedAddress
    )

    # generate random number 500 users
    for i in range(500):
        # Generate fake data
        encryptedName = fake.user_name()
        username = fake.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        ethnicity = ['White', 'Black', 'Asian', 'Hispanic', 'Other'][random.randint(0, 4)]
        birthdate = fake.date_of_birth()

        start_time = time.time()
        # Create MedicalUser object
        user = MedicalUser.objects.create_user(
            encryptedName = encryptedName,
            username = str(i) + username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            ethnicity =  ethnicity,
            birthdate = birthdate,
            address = address
        )
        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print("Elapsed Time for encrypted data: {} seconds".format(elapsed_time))

        start_time = time.time()
        unencryptedUser = UnencryptedMedicalUser.objects.create_user(
            unencryptedName = encryptedName,
            username = str(i) + username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            ethnicity =  ethnicity,
            birthdate = birthdate,
            address = unencryptedAddress
        )
        elapsed_time = time.time() - start_time
        print("Elapsed Time for unencrypted data: {} seconds".format(elapsed_time))

        for _ in range(random.randint(1,100)):
            Appointment.objects.create(
                date = fake.date_time(),
                medical_user = user,
                entity = entity
            )
            UnencryptedAppointment.objects.create(
                date = fake.date_time(),
                unencrypted_medical_user = unencryptedUser,
                unencrypted_entity = unencryptedEntity
            )

    
    return JsonResponse({'message': 'Object generation completed'})

def appointments_by_user(request):
    appointments_data = Appointment.objects.select_related('medical_user', 'entity').annotate(num_appointments=Count('medical_user__appointments')).values('medical_user__encryptedName', 'num_appointments', 'entity__name', 'entity__address__address_line_1', 'entity__address__address_line_2', 'entity__address__city', 'entity__address__post_code')[:1000]
    appointments_list = list(appointments_data)
    return JsonResponse(appointments_list, safe=False)     

def unencrypted_appointment_by_user(request):
    appointments_data = UnencryptedAppointment.objects.select_related('unencrypted_medical_user', 'unencrypted_entity').annotate(num_appointments=Count('unencrypted_medical_user__appointments')).values('unencrypted_medical_user__unencryptedName', 'num_appointments', 'unencrypted_entity__name', 'unencrypted_entity__address__address_line_1', 'unencrypted_entity__address__address_line_2', 'unencrypted_entity__address__city', 'unencrypted_entity__address__post_code')[:1000]
    appointments_list = list(appointments_data)
    return JsonResponse(appointments_list, safe=False) 

from django.contrib.contenttypes.models import ContentType

def account_type(account):
    if account.polymorphic_ctype == ContentType.objects.get_for_model(MedicalPatient):
        return 'MedicalPatient'
    elif account.polymorphic_ctype == ContentType.objects.get_for_model(MedicalProfessional): 
        return 'MedicalProfessional'
    else:
        return 'MedicalEntityManager'


def account_type(account):
    if account.polymorphic_ctype == ContentType.objects.get_for_model(MedicalPatient):
        return 'MedicalPatient'
    elif account.polymorphic_ctype == ContentType.objects.get_for_model(MedicalProfessional): 
        return 'MedicalProfessional'
    elif account.polymorphic_ctype == ContentType.objects.get_for_model(MedicalEntityManager):
        return 'MedicalEntityManager'
    else:
        return "Person"

def create_polymorphic(request):
    print("resetting all models")
    Person.objects.all().delete
    MedicalEntityManager.objects.all().delete()
    MedicalProfessional.objects.all().delete()
    MedicalPatient.objects.all().delete()
    print("Creating instances for polymorphic tests")
    
    # Create a person data
    fake = Faker()
    email = fake.email()
    username = fake.user_name()  # Use fake.user_name() to generate unique usernames
    name = fake.name()
    ethnicity = ['White', 'Black', 'Asian', 'Hispanic', 'Other'][random.randint(0, 4)]
    birthdate = fake.date_of_birth()

    ## first make a customuser object to hold auth details
    c1 = CustomUser.objects.create(email=email, username=username)
    p1 = Person.objects.create(custom_user=c1, name=name, ethnicity=ethnicity, birthdate=birthdate)

    email = fake.email()
    username = fake.user_name()  # Use fake.user_name() to generate unique usernames
    name = fake.name()
    ethnicity = ['White', 'Black', 'Asian', 'Hispanic', 'Other'][random.randint(0, 4)]
    birthdate = fake.date_of_birth()
    c2 = CustomUser.objects.create(email=email, username=username)
    p2 = Person.objects.create(custom_user=c2, name=name, ethnicity=ethnicity, birthdate=birthdate)

    email = fake.email()
    username = fake.user_name()  # Use fake.user_name() to generate unique usernames
    name = fake.name()
    ethnicity = ['White', 'Black', 'Asian', 'Hispanic', 'Other'][random.randint(0, 4)]
    birthdate = fake.date_of_birth()
    c3 = CustomUser.objects.create(email=email, username=username)
    p3 = Person.objects.create(custom_user=c3, name=name, ethnicity=ethnicity, birthdate=birthdate)

    # Create entity manager data
    email = fake.email()
    username = fake.user_name()  # Use fake.user_name() to generate unique usernames
    salary = fake.random_number(digits=5)
    isak_level = fake.random_number(digits=1)
    c4 = CustomUser.objects.create(email=email, username=username)
    MedicalEntityManager.objects.create(custom_user=c4, associated_person=p1, salary=salary, is_super=True)

    # create professional data
    email = fake.email()
    username = fake.user_name()  # Use fake.user_name() to generate unique usernames
    salary = fake.random_number(digits=5)
    isak_level = fake.random_number(digits=1)
    c5 = CustomUser.objects.create(email=email, username=username)
    MedicalProfessional.objects.create(custom_user=c5, associated_person=p2, salary=salary, isak_level=isak_level)

    # make another professional who is the same person as the manager

    # create medical patient data
    email = fake.email()
    username = fake.user_name()  # Use fake.user_name() to generate unique usernames
    disease = fake.word()
    c6 = CustomUser.objects.create(email=email, username=username)
    MedicalPatient.objects.create(custom_user=c6, associated_person=p3, disease=disease)

    return JsonResponse({'message': 'Object generation completed'})



import json

def get_polymorphic(request):
    response = {
        "Managers": [],
        "Professionals": [],
        "Patients": [],
        "Test": []
    }

    # Get managers and their associated persons
    managers = UserLogin.objects.instance_of(MedicalEntityManager)
    for manager in managers:
        response["Managers"].append({
            "name": manager.associated_person.name,
            "email": manager.custom_user.email,
            "salary": manager.salary
        })

    # Get professionals and their associated persons
    professionals = UserLogin.objects.instance_of(MedicalProfessional)
    for professional in professionals:
        response["Professionals"].append({
            "name": professional.associated_person.name,
            "email": professional.custom_user.email,
            "salary": professional.salary,
            "isak_level": professional.isak_level
        })

    # Get patients and their associated persons
    patients = UserLogin.objects.instance_of(MedicalPatient)
    for patient in patients:
        response["Patients"].append({
            "name": patient.associated_person.name,
            "email": patient.custom_user.email,
            "disease": patient.disease
        })

    # Test to see if given a random UserLogin we can determine:
        # 1. The type of account
        # 2. the associated person
    randomLogin = UserLogin.objects.first()
    ctype = ContentType.objects.get_for_id(randomLogin.polymorphic_ctype_id)
    
    if ctype.model == "person":
        associated_person = randomLogin.name
    else:
        associated_person = randomLogin.associated_person.name
    response["Test"].append({'associated_person': associated_person})
    return JsonResponse(response)

def wipe_data(request):
    print("resetting all models")
    Person.objects.all().delete
    MedicalEntityManager.objects.all().delete()
    MedicalProfessional.objects.all().delete()
    MedicalPatient.objects.all().delete()
    UserLogin.objects.all().delete()
    return JsonResponse({"Message": "Deleted"})