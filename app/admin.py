from django.contrib import admin

from .models import Bmi, Contactus, Patient, Test

admin.site.register(Bmi)
admin.site.register(Contactus)
admin.site.register(Patient)
admin.site.register(Test)