# Generated by Django 4.1.3 on 2022-12-20 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_patient_tests_alter_test_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='tests',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
