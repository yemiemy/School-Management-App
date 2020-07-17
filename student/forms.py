from django import forms
from django.contrib.auth import get_user_model
from .models import Student, Parent

User = get_user_model()

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 
            'last_name', 
            'gender',
            'date_of_birth',
            'blood_group',
            'religion', 
            'email',
            'student_class',
            'phone',
            'short_BIO',
            'upload_student_photo'
            ]

class ParentUpdateForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = [
            'first_name', 
            'last_name', 
            'gender',
            'occupation',
            'ward',
            'blood_group',
            'religion', 
            'email',
            'address',
            'phone',
            'short_BIO',
            'upload_parent_photo'
            ]
