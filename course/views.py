from django.shortcuts import render
from django.urls import reverse
from .models import Course, Class
from .forms import CourseUpdateForm
from .utils import id_generator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from student.models import Student, Parent
# Create your views here.

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = [
            'name', 
            'select_class'
            ]
    def form_valid(self, form):
        form.instance.course_code = id_generator()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            # 'object': Course.objects.get(slug=self.kwargs.get('slug')),
            'courses':Course.objects.all().order_by('-id'),
            'classes':Class.objects.all()
        })  
        return context
    def get_success_url(self):
        return reverse('create')


@login_required
def dashboard(request):
    students = Student.objects.all()

    student_count = 0
    for item in students:
        student_count += 1
    
    parents = Parent.objects.all()

    parent_count=0
    for _ in parents:
        parent_count+=1
    context={
        'student_count':student_count,
        'parent_count':parent_count
    }
    return render(request, 'dashboard.html', context)