# Generated by Django 4.2.4 on 2023-11-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_students_age_alter_students_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(max_length=220),
        ),
    ]
