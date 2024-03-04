# users/views.py
import json
import random
from django.http import JsonResponse
from faker import Faker
from django.utils import timezone
from .models import MedicalUser, Address
from .serializers import MedicalUserSerializer

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


def view_users(request):
    print("-------------------- GETTING USERS -----------------------")
    # get all users and convert to json to return
    users = MedicalUser.objects.all.values()
    json_data = json.dumps(list(users))
    return JsonResponse({"message": "Found all these users: ", "users": json_data})


def delete_users(request):
    print("-------------------- DELETING USERS -----------------------")
    # delete all users
    MedicalUser.objects.all().delete()
    Address.objects.all().delete()
    return JsonResponse({'message': 'All users and addresses deleted'})   

def get_users(request, limit=-1):
    if limit == -1:
        medical_users = MedicalUser.objects.all()
    else:
        medical_users = MedicalUser.objects.all()[:limit]
    serializer = MedicalUserSerializer(medical_users, many=True)
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