
from django import forms
from .models import Patient


class PatientRegistrationForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'age', 'email', 'doctor']

    def clean_age(self):
        age = self.cleaned_data['age']

        if age <= 0:
            raise forms.ValidationError(
                "Age must be greater than zero."
            )

        return age
