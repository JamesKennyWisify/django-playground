from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from encrypted_model_fields.fields import EncryptedCharField, EncryptedDateField

class MedicalUser(AbstractUser, models.Model):
    ethnicity = EncryptedCharField(max_length=100)
    birthdate = EncryptedDateField()
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='medical_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='medical_users')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='user_address')
    encryptedName = EncryptedCharField(max_length=255, default='', blank=True, null=True)

class UnencryptedMedicalUser(AbstractUser, models.Model):
    ethnicity = models.CharField(max_length=100)
    birthdate = models.DateField()
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='unencrypted_medical_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='unencrypted_medical_users')
    address = models.ForeignKey('UnencryptedAddress', on_delete=models.CASCADE, related_name='user_unencrypted_address')
    unencryptedName = models.CharField(max_length=255, default='', blank=True, null=True)

class Appointment(models.Model):
    date = models.DateTimeField()
    medical_user = models.ForeignKey(MedicalUser, on_delete=models.CASCADE, related_name='appointments')
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE, related_name='appointments')

class UnencryptedAppointment(models.Model):
    date = models.DateTimeField()
    unencrypted_medical_user = models.ForeignKey(UnencryptedMedicalUser, on_delete=models.CASCADE, related_name='appointments')
    unencrypted_entity = models.ForeignKey('UnencryptedEntity', on_delete=models.CASCADE, related_name='appointments')

class Entity(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='entity_address')

class UnencryptedEntity(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('UnencryptedAddress', on_delete=models.CASCADE, related_name='entity_address')

class Address(models.Model):
    address_line_1 = EncryptedCharField(max_length=255)
    address_line_2 = EncryptedCharField(max_length=255, blank=True, null=True)
    city = EncryptedCharField(max_length=50)
    post_code = EncryptedCharField(max_length=50)

class UnencryptedAddress(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)

class RandomWriteObject(models.Model):
    encryptedName = EncryptedCharField(max_length=255)
    encryptedName2 = EncryptedCharField(max_length=255)
    encryptedName3 = EncryptedCharField(max_length=255)
    encryptedName4 = EncryptedCharField(max_length=255)
    encryptedName5 = EncryptedCharField(max_length=255)
    encryptedName6 = models.CharField(max_length=50)
    encryptedName7 = models.CharField(max_length=50)
    encryptedName8 = models.CharField(max_length=50)
    encryptedName9 = models.CharField(max_length=50)
    encryptedName10 = models.CharField(max_length=50)