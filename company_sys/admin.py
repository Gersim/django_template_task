from django.contrib import admin
from .models import Company,Employee,Job,Vehicle
# Register your models here.

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Vehicle)
