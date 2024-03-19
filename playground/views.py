# users/views.py
import json
import random
import time
from django.http import JsonResponse
from faker import Faker
from django.utils import timezone
from .models import Appointment, Entity, MedicalUser, Address, RandomWriteObject, UnencryptedAddress, UnencryptedAppointment, UnencryptedEntity, UnencryptedMedicalUser
from django.db.models import Count
from .serializers import MedicalUserSerializer, UnencryptedMedicalUserSerializer

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