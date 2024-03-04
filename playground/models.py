from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from encrypted_model_fields.fields import EncryptedCharField

class MedicalUser(AbstractUser, models.Model):
    ethnicity = models.CharField(max_length=100)
    encryptedName = EncryptedCharField(max_length=50)
    birthdate = models.DateField()
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='medical_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='medical_users')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='user_address')

class Appointment(models.Model):
    date = models.DateTimeField()
    medical_user = models.ForeignKey(MedicalUser, on_delete=models.CASCADE, related_name='appointments')
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE, related_name='appointments')

class Entity(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='entity_address')

class Address(models.Model):
    address_line_1 = EncryptedCharField(max_length=255)
    address_line_2 = EncryptedCharField(max_length=255, blank=True, null=True)
    city = EncryptedCharField(max_length=50)
    post_code = EncryptedCharField(max_length=50)