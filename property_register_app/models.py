from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Subdivision(models.Model):
    subdivision_name = models.CharField(max_length=45)
    phone_number = models.BigIntegerField(max_length=11, blank=True, null=True)
    subdivision_type = models.CharField(max_length=45, choices=[("faculty", "faculty"),
                                                                ("department", "department"),
                                                                ("mega-faculty", "mega-faculty"),
                                                                ("other", "other")])
    id_subdivision = models.ForeignKey("Subdivision", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.subdivision_name



class Employee(AbstractUser):
    second_name = models.CharField(max_length=40, blank=True, null=True)
    position = models.CharField(max_length=40, blank=True, null=True)
    start_year = models.IntegerField(max_length=4, blank=True, null=True)
    home_address = models.CharField(max_length=50, blank=True, null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.first_name + " " + self.last_name

    REQUIRED_FIELDS = ['first_name', 'last_name', 'second_name', 'email']
class Unit_of_property(models.Model):
    inventory_number = models.BigIntegerField(unique=True)
    date_of_registration = models.DateField()
    revaluation_year = models.IntegerField(max_length=4, blank=True, null=True)
    cost = models.FloatField()
    lifetime = models.IntegerField()
    def __str__(self):
        return str(self.inventory_number)

class Classroom(models.Model):
    number = models.IntegerField()
    area = models.FloatField()
    appointment = models.CharField(max_length=45, choices=[("lecture", "lecture"),
                                                                ("laboratory", "laboratory"),
                                                                ("staff_only", "staff_only"),
                                                                ("gym", "gym"),
                                                                 ("other", "other")])
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    employee = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Property_liability")
    unit_of_property = models.ManyToManyField(Unit_of_property, through="Property_list")
    def __str__(self):
        return str(self.number)
class Property_liability(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.classroom.__str__() + " " + self.employee.__str__()
class Property_list(models.Model):
    unit_of_property = models.ForeignKey(Unit_of_property, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date_of_creation = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.unit_of_property.__str__() + " " + self.classroom.__str__()