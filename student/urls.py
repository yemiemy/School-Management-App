from django.urls import path
from .views import (
    student_admmision, 
    add_parent,
    StudentListView, 
    StudentDetailView,
    StudentUpdateView,
    ParentListView,
    ParentDetailView,
    ParentUpdateView,
    search,
    search_parent
    )
urlpatterns = [
    path('student-admission/', student_admmision, name='admission'),
    path('add-parent/', add_parent, name='add_parent'),
    path('all-parents/', ParentListView.as_view(), name='all_parent'),
    path('all-students/', StudentListView.as_view(), name='all_student'),
    path('students/<slug>', StudentDetailView.as_view(), name='student'),
    path('students/<slug>/update', StudentUpdateView.as_view(), name='update-student'),
    path('parents/<slug>', ParentDetailView.as_view(), name='parent'),
    path('parents/<slug>/update', ParentUpdateView.as_view(), name='update-parent'),
    path('search/', search, name='search'),
    path('parents/search/', search_parent, name='search_parent'),
]