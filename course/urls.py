from django.urls import path
from .views import CourseCreateView
urlpatterns = [
    path('create-course/', CourseCreateView.as_view(), name='create'),
]