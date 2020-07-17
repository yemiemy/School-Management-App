# Generated by Django 3.0.8 on 2020-07-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('student_class', models.CharField(choices=[('JSS 1 ', 'JSS 1'), ('JSS 2', 'JSS 2'), ('JSS 3', 'JSS 3'), ('SSS 1', 'SSS 1'), ('SSS 2', 'SSS 2'), ('SSS 3', 'SSS 3')], default='Please Select Class *', max_length=50)),
                ('addmission_id', models.CharField(default='ABC', max_length=120, unique=True)),
                ('phone', models.CharField(max_length=50)),
                ('short_BIO', models.TextField(blank=True, null=True)),
                ('upload_student_photo', models.ImageField(default='default.png', upload_to='student_photo/')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('blood_group', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('short_BIO', models.TextField(blank=True, null=True)),
                ('upload_parent_photo', models.ImageField(default='default.png', upload_to='parent_photo/')),
                ('ward', models.ManyToManyField(blank=True, null=True, to='student.Student')),
            ],
        ),
    ]
