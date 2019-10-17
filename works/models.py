from django.db import models
from django.contrib import admin

class Work(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000, blank=True)
    link = models.CharField(max_length=128, blank=True)
    doctor = models.CharField(max_length=128, blank=True)
    active = models.BooleanField(default=True)
    main_image1= models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    main_image2= models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    main_image3= models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    resume = models.TextField(max_length=2500, blank=True)

    def __str__(self):      
        return self.title

class WorkImage(models.Model):
    work = models.ForeignKey(Work)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=900, blank = True)
    work_number = models.IntegerField(default=0)
    title = models.CharField(max_length=200, blank=True)
    desc = models.TextField(max_length=2500, blank=True)
	
    def __str__(self):     
        return self.title