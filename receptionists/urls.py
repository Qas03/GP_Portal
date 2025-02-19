from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.manage_patient_records, name='manage_patient_records'),
    path('appointments/book/', views.book_appointment, name='book_appointment'),
    path('appointments/cancel/<str:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
]