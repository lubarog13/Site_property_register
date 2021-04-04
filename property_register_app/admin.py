from django.contrib import admin
from .models import Employee, Unit_of_property, Subdivision, Classroom, Property_list, Property_liability
admin.site.register(Employee)
admin.site.register(Unit_of_property)
admin.site.register(Subdivision)
admin.site.register(Classroom)
admin.site.register(Property_list)
admin.site.register(Property_liability)
# Register your models here.
