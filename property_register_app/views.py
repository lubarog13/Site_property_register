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
class EmployeeAPIView(APIView):
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