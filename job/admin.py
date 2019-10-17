from django.contrib import admin
from job.models import Vacancy, VacancyAdmin

admin.site.register(Vacancy, VacancyAdmin)
