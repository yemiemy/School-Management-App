# Generated by Django 3.0.8 on 2020-07-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200717_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='select_class',
            field=models.CharField(choices=[('All Classes ', 'All Classes'), ('Junior Class ', 'Junior Class'), ('JSS 1 ', 'JSS 1'), ('JSS 2', 'JSS 2'), ('JSS 3', 'JSS 3'), ('Senior Class', 'Senior Class'), ('SSS 1', 'SSS 1'), ('SSS 2', 'SSS 2'), ('SSS 3', 'SSS 3')], max_length=120),
        ),
    ]
