from django.db import models

from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

CLASS_CHOICES = (
    ('All Classes ', 'All Classes'),
    ('Junior Class ', 'Junior Class'),
    ('JSS 1 ', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
    ('Senior Class', 'Senior Class'),
    ('SSS 1', 'SSS 1'),
    ('SSS 2', 'SSS 2'),
    ('SSS 3', 'SSS 3')
)

class Class(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=120)
    select_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    course_code = models.CharField(max_length=120, default='001', unique=True)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=120,
    )
    date_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
      

    class Meta:
        unique_together = ('name', 'slug')

    # def get_absolute_url(self):
    #     kwargs = {
    #         'slug': self.slug
    #     }
    #     return reverse('course_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)