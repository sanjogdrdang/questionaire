# Generated by Django 4.1.3 on 2022-12-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_patient_height_patient_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bmi',
            field=models.IntegerField(default=0),
        ),
    ]