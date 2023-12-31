# Generated by Django 4.2.4 on 2023-11-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
