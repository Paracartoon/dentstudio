from django.contrib import admin
from staff.models import Staff, StaffAdmin

admin.site.register(Staff, StaffAdmin)