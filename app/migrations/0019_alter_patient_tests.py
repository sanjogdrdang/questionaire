# Generated by Django 4.1.3 on 2022-12-20 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_patient_tests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='tests',
            field=models.CharField(default='', max_length=20),
        ),
    ]
