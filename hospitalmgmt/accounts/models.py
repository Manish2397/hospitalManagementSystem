from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Profile(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    @staticmethod
    def toGender(key):
        for item in Profile.GENDER:
            if item[0] == key:
                return item[1]
        return "None"

    firstname = models.CharField(blank=True, max_length=50)
    lastname = models.CharField(blank=True, max_length=50)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    phone = models.CharField(blank=True, max_length=20)
    allergies = models.CharField(blank=True, max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Account(models.Model):
    # ACCOUNT_UNKNOWN = 0
    # ACCOUNT_PATIENT = 10
    # ACCOUNT_NURSE = 20
    # ACCOUNT_DOCTOR = 30
    # ACCOUNT_ADMIN = 40
    ACCOUNT_TYPES = (
        ("Patient", "Patient"),
        ("HR","HR"),
        ("Doctor", "Doctor"),
        ("Receptionist", "Receptionist"),
    )
    # EMPLOYEE_TYPES = (
    #     (ACCOUNT_NURSE, "Nurse"),
    #     (ACCOUNT_DOCTOR, "Doctor"),
    #     (ACCOUNT_ADMIN, "Admin"),
    # )
    #
    # @staticmethod
    # def toAccount(key):
    #     """
    #     Parses an integer value to a string representing an account role.
    #     :param key: The account role
    #     :return: The string representation of the name for the account role
    #     """
    #     for item in Account.ACCOUNT_TYPES:
    #         if item[0] == key:
    #             return item[1]
    #     return "None"

    role = models.CharField(default="None", choices=ACCOUNT_TYPES,max_length=20)
    profile = models.OneToOneField(Profile,on_delete=models.PROTECT)
    user = models.OneToOneField(User,on_delete=models.PROTECT)


class Prescription(models.Model):
    patient = models.ForeignKey(User,on_delete=models.PROTECT,related_name="patient")
    doctor = models.ForeignKey(User, on_delete=models.PROTECT,related_name="doctor")
    date = models.DateField(auto_now_add=True)
    medication = models.CharField(max_length=100)
    instruction = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.patient.username + " - " + self.doctor.username

class Appointment(models.Model):
    doctor = models.ForeignKey(User, related_name="doctors",on_delete=models.PROTECT)
    patient = models.ForeignKey(User, related_name="patients",on_delete=models.PROTECT)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    startTime = models.TimeField()
    endTime = models.TimeField()
    date = models.DateField()
    cost=models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.patient.username +" - "+ self.doctor.username