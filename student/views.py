from django.shortcuts import render, redirect
from .utils import id_generator
from .models import Student, Parent
from .forms import StudentUpdateForm, ParentUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView
from course.models import Course, Class
# Create your views here.

@login_required
def student_admmision(request):
    if request.method == 'POST':
        p_form = StudentUpdateForm(
            request.POST, 
            request.FILES 
            )

        if p_form.is_valid():
            new_admmision = p_form.save(commit=False)
            new_admmision.admission_id = id_generator()
            new_admmision.save()
            messages.success(
                request, 'You have successfully added a new student!'
                )
            return redirect('all_student')
    else:
        p_form = StudentUpdateForm()
    classes = Class.objects.all()
    return render(request, 'student/admission.html', {'p_form':p_form, 'classes':classes})

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    ordering = ['-id']
    paginate_by = 15

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'courses': Course.objects.all(),
            # 'class': Class.objects.get(),
        })  
        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
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
    template_name = 'student/admission.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object': Student.objects.get(slug=self.kwargs.get('slug')),
        })  
        return context

def add_parent(request):
    students = Student.objects.all()
    if request.method == 'POST':
        p_form = ParentUpdateForm(
            request.POST, 
            request.FILES 
            )

        if p_form.is_valid():
            p_form.save()
            messages.success(
                request, 'You have successfully added a new parent!'
                )
            return redirect('add_parent')
    else:
        p_form = ParentUpdateForm()
    
    context = {
        'p_form':p_form, 
        'students':students
        } 
    return render(request, 'student/add_parent.html', context)

class ParentListView(LoginRequiredMixin, ListView):
    model = Parent
    context_object_name = 'parents'
    ordering = ['-id']
    paginate_by = 4

class ParentDetailView(LoginRequiredMixin, DetailView):
    model = Parent

class ParentUpdateView(LoginRequiredMixin, UpdateView):
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
    template_name = 'student/add_parent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object': Parent.objects.get(slug=self.kwargs.get('slug')),
            'students': Student.objects.all().order_by('-id')
        })  
        return context

def search(request):
    if request.method == 'GET':
        admission_id = request.GET['admission_id']
        name = request.GET['name']
        student_class = request.GET['class']
        if admission_id == '':
            admission_id = 'none'
        if name == '':
            name = 'none'
        if student_class == '':
            student_class = 'none'

        result = Student.objects.filter(admission_id__icontains=admission_id)|Student.objects.filter(first_name__icontains = name)|Student.objects.filter(student_class__icontains=student_class)

        context = {
            'result':result,
            'admission_id':admission_id,
            'name':name,
            'student_class':student_class
        }
        return render(request, 'student/search.html', context)


def search_parent(request):
    if request.method == 'GET':
        phone = request.GET['phone']
        name = request.GET['name']
        occupation = request.GET['occupation']
        if phone == '':
            phone = 'none'
        if name == '':
            name = 'none'
        if occupation == '':
            occupation = 'none'

        result = Parent.objects.filter(phone__icontains=phone)|Parent.objects.filter(first_name__icontains = name)|Parent.objects.filter(occupation__icontains=occupation)

        context = {
            'result':result,
        }
        return render(request, 'student/search-parent.html', context)
