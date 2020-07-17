from django import forms
from django.contrib.auth import get_user_model
from .models import Course

User = get_user_model()

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name', 
            'select_class'
            ]
