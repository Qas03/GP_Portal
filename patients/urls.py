from django.urls import path
from . import views

urlpatterns = [
    path('<str:patient_id>/portal/', views.self_service_portal, name='self_service_portal'),
    path('<str:patient_id>/profile/', views.view_patient_profile, name='view_patient_profile'),
]