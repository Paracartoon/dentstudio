from django.db import models
from django.contrib import admin

class Vacancy(models.Model):
    position = models.CharField(max_length=128)
    description = models.TextField(max_length=2500, blank=True)
    skills = models.TextField(max_length=2500, blank=True)
	
    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):      
        return self.position

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('position', 'description', 'skills')
	
    def __str__(self):     
        return self.position

