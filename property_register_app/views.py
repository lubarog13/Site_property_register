from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from property_register_app.models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from .serialisers import *
# Create your views here.

# class SubdivisionList(ListView):
#     model = Subdivision
#     template_name = "property_register_app/subdivision_view.html"
# class Subdivision_view(DetailView):
#     model = Subdivision
# class SubdivisionCreateView(CreateView):
#     model = Subdivision
#     fields = [
#         "subdivision_name",
#         "phone_number",
#         "subdivision_type",
#         "id_subdivision"
#     ]
#     success_url = '/subdivision/'
class SubdivisionAPICreateView(APIView):
    def post(self, request):
        subdivision = request.data.get("subdivision")
        serializer = SubdivisionCreateSerializer(data=subdivision)

        if serializer.is_valid(raise_exception=True):
            subdivision_saved = serializer.save()

        return Response({"Success": "Subdivision '{}' created succesfully.".format(subdivision_saved.title)})

# class SubdivisionUpdateView(UpdateView):
#     model = Subdivision
#     fields = [
#         "subdivision_name",
#         "phone_number",
#         "subdivision_type",
#         "id_subdivision"
#     ]
#     success_url = '/subdivision/'
# class SubdivisionDeleteView(DeleteView):
#     model = Subdivision
#     success_url = '/subdivision/'
# def classroom_list(request, id_subdivision):
#     context = {}
#     context["subd"] = Subdivision.objects.get(pk=id_subdivision)
#     context["dataset"] = Classroom.objects.filter(subdivision = id_subdivision)
#     return render(request, "property_register_app/classroom_view.html", context=context)
# class ClassroomView(DetailView):
#     model = Classroom
# class ClassroomAllView(ListView):
#     model = Classroom
#     template_name = "property_register_app/classroom_list.html"
# class ClassroomCreateView(CreateView):
#     model = Classroom
#     fields = [
#         "number",
#         "area",
#         "appointment",
#         "subdivision",
#         "employee",
#     ]
#     success_url = '/classrooms_all/'
# class ClassroomUpdateView(UpdateView):
#     model = Classroom
#     fields = [
#         "number",
#         "area",
#         "appointment",
#         "subdivision",
#         "employee",
#     ]
#     success_url = '/classrooms_all/'
# class ClassroomDeleteView(DeleteView):
#     model = Classroom
#     success_url = '/classrooms_all/'
class SubdivisionAPIView(APIView):
    def get(self, request):
        subdivisions = Subdivision.objects.all()
        serializer = SubdivisionSerializer(subdivisions, many=True)
        return Response({"Subdivisions": serializer.data})
class ClassroomsAPIView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response({"Classrooms": serializer.data})
class EmployeesAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"Employees": serializer.data})
class UnitOfPropertyAPIView(APIView):
    def get(self, request):
        property = Unit_of_property.objects.all()
        serializer = UnitOfPropertySerializer(property, many=True)
        return Response({"Unit of property: ": serializer.data})
class ClassroomListAPIView(ListAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
class ClassroomCreateAPIView(CreateAPIView):
    serializer_class = ClassroomCreateSerializer
    queryset = Classroom.objects.all()
class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeCreateSerializer
    queryset = Employee.objects.all()
class PropertyLiabilityCreateAPIView(CreateAPIView):
    serializer_class = PropertyLiabilityCreateSerializer
    queryset = Property_liability.objects.all()
class PropertyListCreateAPIView(CreateAPIView):
    serializer_class = PropertyListCreateSerializer
    queryset = Property_list.objects.all()
class UnitOfPropertyCreateApiView(CreateAPIView):
    serializer_class = UnitOfPropertyCreateSerializer
    queryset = Unit_of_property.objects.all()


class ClassroomUpdateAPIView(UpdateAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()

class ClassroomRetrieveAPIView(RetrieveAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()


class ClassroomDeleteAPIView(DestroyAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()


class EmloyeeUpdateAPIView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmloyeeRetriveAPIView(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmloyeeDeleteAPIView(DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class PropertyLiabilityUpdateAPIView(UpdateAPIView):
    serializer_class = PropertyLiabilityCreateSerializer
    queryset = Property_liability.objects.all()


class PropertyLiabilityRetrieveAPIView(RetrieveAPIView):
    serializer_class = PropertyLiabilitySerializer
    queryset = Property_liability.objects.all()

class PropertyLiabilityDeleteAPIView(DestroyAPIView):
    serializer_class = PropertyLiabilityCreateSerializer
    queryset = Property_liability.objects.all()


class UnitOfPropertyUpdateAPIView(UpdateAPIView):
    serializer_class = UnitOfPropertySerializer
    queryset = Unit_of_property.objects.all()

class UnitOfPropertyRetrieveAPIView(RetrieveAPIView):
    serializer_class = UnitOfPropertySerializer
    queryset = Unit_of_property.objects.all()

class UnitOfPropertyDeleteAPIView(DestroyAPIView):
    serializer_class = UnitOfPropertySerializer
    queryset = Unit_of_property.objects.all()

class PropertyListUpdateAPIView(UpdateAPIView):
    serializer_class = PropertyListCreateSerializer
    queryset = Property_list.objects.all()

class PropertyListRetrieveAPIView(RetrieveAPIView):
    serializer_class = PropertyListCreateSerializer
    queryset = Property_list.objects.all()

class PropertyListDeleteAPIView(DestroyAPIView):
    serializer_class = PropertyListCreateSerializer
    queryset = Property_list.objects.all()
class SubdivisionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
class ClassesASubdivision(APIView):
    def get(self, request, id_subd):
        classrooms = Classroom.objects.filter(subdivision = id_subd)
        subdivisions = Subdivision.objects.filter(id_subdivision = id_subd)
        employees = Employee.objects.filter(Q(subdivision__in=subdivisions) | Q(subdivision = id_subd))
        serializer = ClassroomSerializer(classrooms, many=True)
        serializer1 = SubdivisionSerializer(subdivisions, many=True)
        serializer2 = EmployeeSerializer(employees, many=True)
        return Response({"Classrooms": serializer.data, "Subdivisions": serializer1.data, "Employees": serializer2.data})

class ClassroomAPIView(APIView):
    def get(self, request, id_class):
        classroom = Classroom.objects.get(pk=id_class)
        serializer = ClassroomSerializer(classroom, many=False)
        property_liabilities = Property_liability.objects.filter(classroom=id_class)
        serializer_e = PropertyLiabilitySerializer(property_liabilities, many=True)
        print(serializer_e.data)
        return Response({"Classroom":serializer.data, "Employees": serializer_e.data})
class EmployeeAPIView(APIView):
    def get(self, request, id_employee):
        employee = Employee.objects.get(pk=id_employee)
        serializer = EmployeeSerializer(employee, many=False)
        classrooms = Classroom.objects.filter(employee = employee)
        property_lists = Property_list.objects.filter(classroom__in = classrooms)
        serializer1 = PropertyListSerializer(property_lists, many=True)
        return  Response({"Employee": serializer.data, "Property_list": serializer1.data})
class SearchAPIView(APIView):
    def get(self, request, search_string):
        employee = Employee.objects.filter(Q(first_name__contains=search_string) | Q(last_name__contains=search_string) | Q(second_name__contains=search_string) | Q(position__contains=search_string))
        serializer = EmployeeSerializer(employee, many=True)
        try:
            classroom = Classroom.objects.filter(Q(appointment__contains=search_string) | Q(number__contains=(int)(search_string)))
        except ValueError:
            classroom = Classroom.objects.filter(appointment__contains=search_string)
        serializer1 = ClassroomSerializer(classroom, many=True)
        subdivision = Subdivision.objects.filter(Q(subdivision_name__contains=search_string) | Q(subdivision_type__contains=search_string))
        serializer2 = SubdivisionSerializer(subdivision, many=True)
        try:
            unitOfProperty = Unit_of_property.objects.filter(inventory_number__contains=(int)(search_string))
        except ValueError:
            unitOfProperty = None
        serializer3 = UnitOfPropertySerializer(unitOfProperty, many=True)
        return Response({"Employee": serializer.data, "Classroom": serializer1.data, "Subdivision":serializer2.data, "Unit_of_property":serializer3.data})
class PropertyAPIView(APIView):
    def get(self, request, id_un):
        unit_of_property = Unit_of_property.objects.get(pk=id_un)
        classrooms = Classroom.objects.filter(unit_of_property=unit_of_property)
        serializer = UnitOfPropertyCreateSerializer(unit_of_property, many=False)
        serializer1 = ClassroomSerializer(classrooms, many=True)
        return Response({"Classroom":serializer1.data, "Unit_of_property": serializer.data})