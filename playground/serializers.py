from rest_framework import serializers
from .models import MedicalUser, UserLogin

class MedicalUserSerializer(serializers.ModelSerializer):
    birthdate = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = MedicalUser
        fields = '__all__'

class UnencryptedMedicalUserSerializer(serializers.ModelSerializer):
    birthdate = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = MedicalUser
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLogin
        fields = '__all__'