# Generated by Django 4.1.3 on 2023-01-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_patient_answer2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='specificanswer1',
            field=models.CharField(default='non', max_length=200),
        ),
    ]
