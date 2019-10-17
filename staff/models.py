from django.db import models
from django.contrib import admin

class Staff(models.Model):
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128, blank=True)
    description = models.TextField(max_length=2500, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'persons'

    def __str__(self):      
        return self.name

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'description', 'image', 'link')
	
    def __str__(self):     
        return self.name
