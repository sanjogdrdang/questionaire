# Generated by Django 4.1.3 on 2022-12-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_patient_diet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='diet',
            new_name='diet_answer',
        ),
        migrations.AddField(
            model_name='patient',
            name='diet_question',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
