
from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),

    path('patients/', views.patient_list, name='patient_list'),

    path(
        'patients/register/',
        views.patient_register,
        name='patient_register'
    ),
]
