from rest_framework import serializers
from .models import MedicalUser

class MedicalUserSerializer(serializers.ModelSerializer):
    birthdate = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = MedicalUser
        fields = '__all__'