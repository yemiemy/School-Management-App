from django.db import models

from django.utils.text import slugify
from django.urls import reverse
from course.models import Class
# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

CLASS_CHOICES = (
    ('JSS 1 ', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
    ('SSS 1', 'SSS 1'),
    ('SSS 2', 'SSS 2'),
    ('SSS 3', 'SSS 3')
)


class Student(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    email = models.EmailField()
    student_class = models.ForeignKey(Class,on_delete=models.SET_NULL, null=True,default='Please Select Class *')
    admission_id = models.CharField(max_length=120, default='ABC', unique=True)
    phone = models.CharField(max_length=50)
    short_BIO = models.TextField(blank=True, null=True)
    upload_student_photo = models.ImageField(default='default.png', upload_to='student_photo/')
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=120,
    )
    date_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
      

    class Meta:
        unique_together = ('first_name', 'slug')

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('student', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.first_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Parent(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=50)
    ward = models.ManyToManyField(Student, blank=True)
    blood_group = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    short_BIO = models.TextField(blank=True, null=True)
    upload_parent_photo = models.ImageField(default='default.png', upload_to='parent_photo/')
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=120,
    )
        
    def __str__(self):
        return self.first_name
    
    

    class Meta:
        unique_together = ('first_name', 'slug')

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('parent', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.first_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)