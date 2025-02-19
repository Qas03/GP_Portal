from django.shortcuts import render
from GP_Portal.firebase_services import (
    get_document,
    query_collection,
    upload_file_to_storage,
    update_document
)
from firebase_admin import firestore

def doctor_profile(request, doctor_id):
    """
    Function to display the doctor's profile and schedule.
    """
    # Retrieve doctor details from Firestore
    doctor = get_document('doctors', doctor_id)

    # Retrieve appointments associated with the doctor
    appointments = query_collection('appointments', [('doctor_id', '==', doctor_id)])

    # Check if doctor exists
    if not doctor:
        return render(request, 'doctors/error.html', {
            'message': f'Doctor with ID {doctor_id} not found.'
        })

    # Render the doctor's profile and appointments
    return render(request, 'doctors/doctor_profile.html', {
        'doctor': doctor,
        'appointments': appointments
    })


def upload_patient_data(request, patient_id):
    """
    Function for a doctor to upload patient data (medical notes, prescription, and documents).
    """
    if request.method == 'POST':
        # Retrieve form data
        medical_notes = request.POST.get('medical_notes', '')
        prescription = request.POST.get('prescription', '')
        uploaded_file = request.FILES.get('document', None)

        # Initialize file_url to None
        file_url = None

        # If a file is uploaded, process and upload it to Firebase Storage
        if uploaded_file:
            file_name = uploaded_file.name
            file_path = f"patient_documents/{patient_id}/{file_name}"
            file_url = upload_file_to_storage(uploaded_file, file_path)  # Upload the file

        # Update Firestore with the new patient data
        update_document('patients', patient_id, {
            'medical_notes': medical_notes,
            'prescription': prescription,
            'documents': firestore.ArrayUnion(
                [{'name': file_name, 'url': file_url}]
            ) if file_url else []
        })

        # Redirect to success page or show a success message
        return render(request, 'doctors/success.html', {'message': 'Patient data uploaded successfully.'})

    # Render the upload form if it's a GET request
    return render(request, 'doctors/upload_patient_data.html', {'patient_id': patient_id})