from django.urls import path
from . import views  # Import the views from the doctors app

urlpatterns = [
    # URL for viewing a doctor's profile
    path('<str:doctor_id>/profile/', views.doctor_profile, name='doctor_profile'),
    
    # URL for uploading patient data by the doctor
    path('<str:patient_id>/upload_data/', views.upload_patient_data, name='upload_patient_data'),
]