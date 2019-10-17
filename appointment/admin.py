from django.contrib import admin
from appointment.models import Doctor, DoctorAdmin, Reason, ReasonAdmin, Daytime, DaytimeAdmin


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Reason, ReasonAdmin)
admin.site.register(Daytime, DaytimeAdmin)