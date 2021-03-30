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
    id_subdivision = models.ForeignKey("Subdivision", on_delete=models.CASCADE)
    def __str__(self):
        return self.subdivision_name
class Employee(AbstractUser):
    second_name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    start_year = models.IntegerField(max_length=4)
    home_address = models.CharField()
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + " " + self.second_name + " " +self.last_name

    REQUIRED_FIELDS = ['first_name', 'last_name']
class Unit_of_property(models.Model):
    inventory_number = models.BigIntegerField(unique=True)
    date_of_registration = models.DateField()
    revaluation_year = models.IntegerField(max_length=4, blank=True, null=True)
    value_after_revaluation = models.FloatField()
    lifetime = models.IntegerField()
    def __str__(self):
        return self.inventory_number

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
        return self.number
class Property_liability(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.classroom + " " + self.employee
class Property_list(models.Model):
    unit_of_property = models.ForeignKey(Unit_of_property, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date_of_creation = models.DateField()
    def __str__(self):
        return self.unit_of_property + " " + self.classroom