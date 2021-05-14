from django.urls import path
from property_register_app import views

urlpatterns = [
    # path('subdivision/', views.SubdivisionList.as_view(), name='sub_list'),
     path('subdivision/<int:pk>/', views.SubdivisionRetrieveAPIView.as_view(), name = 'sub_view'),
    # path('subdivision_create/', views.SubdivisionCreateView.as_view(), name = 'sub_create'),
    # path('subdivision/<int:pk>/update/', views.SubdivisionUpdateView.as_view(), name = 'sub_update'),
    # path('subdivision/<int:pk>/delete/', views.SubdivisionDeleteView.as_view(), name = 'sub_delete'),
     path('classrooms/<int:id_subd>/', views.ClassesASubdivision.as_view(), name = 'class_list'),
    # path('classroom/<int:pk>/', views.ClassroomView.as_view(), name = 'class_view'),
    # path('classroom_create/', views.ClassroomCreateView.as_view(), name='class_create'),
    # path('classrooms_all/', views.ClassroomAllView.as_view(), name = 'class_all'),
    # path('classroom/<int:pk>/update', views.ClassroomUpdateView.as_view(), name='class_up'),
    # path('classroom/<int:pk>/delete', views.ClassroomDeleteView.as_view(), name='class_del'),
    path('subdivisions/', views.SubdivisionAPIView.as_view(), name='sub_api'),
    path('subdivisions/create/', views.SubdivisionAPICreateView.as_view(), name='sub_api_create'),
    path('classroom/', views.ClassroomListAPIView.as_view(), name='class_api'),
    path('employees/', views.EmployeeAPIView.as_view(), name='employee_api'),
    path('property/', views.UnitOfPropertyAPIView.as_view(), name='property_api'),
    path('property/create/', views.UnitOfPropertyCreateApiView.as_view(), name='property_api_create'),
    path('employees/create/', views.EmployeeCreateAPIView.as_view(), name='employee_api_create'),
    path('classroom/create', views.ClassroomCreateAPIView.as_view(), name='class_api_create'),
    path('property_liab/create/', views.PropertyLiabilityCreateAPIView.as_view(), name='prop_liab_create'),
    path('property_list/create/', views.PropertyListCreateAPIView.as_view(), name='prop_liab_create'),
]