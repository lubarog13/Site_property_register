from django.urls import path
from property_register_app import views

urlpatterns = [
    path('subdivision/', views.SubdivisionList.as_view(), name='sub_list'),
    path('subdivision/<int:pk>/', views.Subdivision_view.as_view(), name = 'sub_view'),
    path('subdivision_create/', views.SubdivisionCreateView.as_view(), name = 'sub_create'),
    path('subdivision/<int:pk>/update/', views.SubdivisionUpdateView.as_view(), name = 'sub_update'),
    path('subdivision/<int:pk>/delete/', views.SubdivisionDeleteView.as_view(), name = 'sub_delete'),
    path('classrooms/<int:id_subdivision>/', views.classroom_list, name = 'class_list'),
    path('classroom/<int:pk>/', views.ClassroomView.as_view(), name = 'class_view'),
    path('classroom_create/', views.ClassroomCreateView.as_view(), name='class_create'),
]