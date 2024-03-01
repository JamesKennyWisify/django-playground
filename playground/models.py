from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class MedicalUser(AbstractUser):
    ethnicity = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
     # Add related_name to groups and user_permissions fields
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='medical_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='medical_users')

class Appointment(models.Model):
    date = models.DateTimeField()
    # Add other appointment-related fields as needed

class Entity(models.Model):
    name = models.CharField(max_length=100)
    # Add other entity-related fields as needed

class Address(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    # Add other address-related fields as needed
