from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django_cryptography.fields import encrypt
from polymorphic.models import PolymorphicModel
import uuid


USER_TYPE_CHOICES = [
    (0, "Person"),
    (1, "Entity Manager"),
    (2, "Entity Professional"),
    (3, "Entity Patient")
]

class UserLogin(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='user_login_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='user_login_permissions')
    user_type = models.SmallIntegerField(choices=USER_TYPE_CHOICES, null=False, default=0)

class Person(UserLogin): 
    ethnicity = encrypt(models.CharField(max_length=100))
    birthdate = encrypt(models.DateField())
    name = encrypt(models.CharField(max_length=100))
 
class MedicalProfessional(UserLogin):
    associated_person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='medical_professional_userlogin')
    salary = encrypt(models.CharField(max_length=100))
    isak_level = encrypt(models.CharField(max_length=100))

class MedicalEntityManager(UserLogin):
    associated_person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='medical_manager_userlogin')
    salary = encrypt(models.CharField(max_length=100))
    is_super = encrypt(models.CharField(max_length=100)) 

class MedicalPatient(UserLogin):
    associated_person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='medical_patient_userlogin')
    disease = encrypt(models.CharField(max_length=100))

class UnencryptedMedicalUser(AbstractUser, models.Model):
    ethnicity = models.CharField(max_length=100)
    birthdate = models.DateField()
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='unencrypted_medical_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='unencrypted_medical_users')
    address = models.ForeignKey('UnencryptedAddress', on_delete=models.CASCADE, related_name='user_unencrypted_address')
    unencryptedName = models.CharField(max_length=255, default='', blank=True, null=True)


class MedicalUser(AbstractUser, models.Model):
    ethnicity = encrypt(models.CharField(max_length=100))
    birthdate = encrypt(models.DateField())
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='medical_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='medical_users')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='user_address')
    encryptedName = encrypt(models.CharField(max_length=255, default='', blank=True, null=True))

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
    address_line_1 = encrypt(models.CharField(max_length=255))
    address_line_2 = encrypt(models.CharField(max_length=255, blank=True, null=True))
    city = encrypt(models.CharField(max_length=50))
    post_code = encrypt(models.CharField(max_length=50))

class UnencryptedAddress(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)

class RandomWriteObject(models.Model):
    encryptedName = encrypt(models.CharField(max_length=255))
    encryptedName2 = encrypt(models.CharField(max_length=255))
    encryptedName3 = encrypt(models.CharField(max_length=255))
    encryptedName4 = encrypt(models.CharField(max_length=255))
    encryptedName5 = encrypt(models.CharField(max_length=255))
    encryptedName6 = models.CharField(max_length=50)
    encryptedName7 = models.CharField(max_length=50)
    encryptedName8 = models.CharField(max_length=50)
    encryptedName9 = models.CharField(max_length=50)
    encryptedName10 = models.CharField(max_length=50)