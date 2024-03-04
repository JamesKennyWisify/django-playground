# users/views.py
import json
import random
from django.http import JsonResponse
from faker import Faker
from django.utils import timezone
from .models import MedicalUser

def generate_users(request):
    fake = Faker()
    print("MAKING USERS --------------------------------------------")
    # Generate 100 users
    for _ in range(100):
        # Generate fake data
        encryptedName = fake.user_name()
        username = fake.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        ethnicity = fake.word()
        birthdate = fake.date_of_birth()

        # Create MedicalUser object
        user = MedicalUser.objects.create_user(
            encryptedName = encryptedName,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            ethnicity=ethnicity,
            birthdate=birthdate,
        )
    return JsonResponse({'message': 'User generation completed'})


def view_users(request):
    print("-------------------- GETTING USERS -----------------------")
    # get all users and convert to json to return
    users = MedicalUser.objects.all.values()
    json_data = json.dumps(list(users))
    return JsonResponse({"message": "Found all these users: ", "users": json_data})


    
