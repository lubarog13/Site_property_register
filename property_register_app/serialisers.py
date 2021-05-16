from rest_framework import serializers
from .models import *
class SubdForeignKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields="__all__"
class SubdivisionSerializer(serializers.ModelSerializer):
    id_subdivision = SubdForeignKeySerializer(many=False)
    class Meta:
        model = Subdivision
        fields="__all__"
class SubdivisionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subdivision
        fields = "__all__"
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields="__all__"

class UnitOfPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_of_property
        fields="__all__"

class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
class PropertyLiabilityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_liability
        fields = "__all__"


class ClassroomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields="__all__"


class PropertyListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_liability
        fields = "__all__"


class UnitOfPropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_of_property
        fields = "__all__"
class ClassroomSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True)
    unit_of_property = UnitOfPropertySerializer(many=True)
    subdivision = SubdivisionSerializer(many=False)
    class Meta:
        model=Classroom
        fields = "__all__"

class PropertyLiabilitySerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False)
    class Meta:
        model=Property_liability
        fields = "__all__"