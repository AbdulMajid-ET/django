
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Patient
from .forms import PatientRegistrationForm


def doctor_list(request):
    doctors = Doctor.objects.all()

    return render(request, 'hospital/doctor_list.html', {
        'doctors': doctors
    })


def patient_list(request):
    doctor_id = request.GET.get('doctor_id')

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    selected_doctor = None

    if doctor_id:
        selected_doctor = get_object_or_404(
            Doctor, id=doctor_id
        )
        patients = patients.filter(doctor=selected_doctor)

    return render(request, 'hospital/patient_list.html', {
        'doctors': doctors,
        'patients': patients,
        'selected_doctor': selected_doctor
    })


def patient_register(request):

    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)

        if form.is_valid():
            patient = form.save()
            return redirect(
                f'/patients/?doctor_id={patient.doctor_id}'
            )

    else:
        form = PatientRegistrationForm()

    return render(request, 'hospital/patient_register.html', {
        'form': form
    })

