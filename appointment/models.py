from django.db import models
from django import forms
from django.contrib import admin
import datetime

class Doctor(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):      
        return self.title

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('title',)
	
    def __str__(self):     
        return self.title
		
class Reason(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):      
        return self.title

class ReasonAdmin(admin.ModelAdmin):
    list_display = ('title',)
	
    def __str__(self):     
        return self.title
		
class Daytime(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):      
        return self.title

class DaytimeAdmin(admin.ModelAdmin):
    list_display = ('title',)
	
    def __str__(self):     
        return self.title
		

class Appointment(models.Model):
  
    def __str__(self):      
        return self.title