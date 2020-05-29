from django.contrib import admin



# Register your models here.
from .models import Profile,Account,Prescription,Appointment

admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Prescription)
admin.site.register(Appointment)