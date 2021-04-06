from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from property_register_app.models import *
# Create your views here.

class SubdivisionList(ListView):
    model = Subdivision
    template_name = "property_register_app/subdivision_view.html"
class Subdivision_view(DetailView):
    model = Subdivision
class SubdivisionCreateView(CreateView):
    model = Subdivision
    fields = [
        "subdivision_name",
        "phone_number",
        "subdivision_type",
        "id_subdivision"
    ]
    success_url = '/subdivision/'
class SubdivisionUpdateView(UpdateView):
    model = Subdivision
    fields = [
        "subdivision_name",
        "phone_number",
        "subdivision_type",
        "id_subdivision"
    ]
    success_url = '/subdivision/'
class SubdivisionDeleteView(DeleteView):
    model = Subdivision
    success_url = '/subdivision/'
def classroom_list(request, id_subdivision):
    context = {}
    context["subd"] = Subdivision.objects.get(pk=id_subdivision)
    context["dataset"] = Classroom.objects.filter(subdivision = id_subdivision)
    return render(request, "property_register_app/classroom_view.html", context=context)
class ClassroomView(DetailView):
    model = Classroom
class ClassroomCreateView(CreateView):
    model = Classroom
    fields = [
        "number",
        "area",
        "appointment",
        "subdivision",
    ]
    success_url = '/subdivision/'