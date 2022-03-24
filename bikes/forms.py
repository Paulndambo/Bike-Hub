from django import forms 
from . models import Employee
from django.contrib.auth.models import User

gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["user", "name", "gender", "id_number", "phone_number", "address", "city", "country"]

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=gender, attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }


   