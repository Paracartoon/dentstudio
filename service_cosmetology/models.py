from django.db import models
from django.contrib import admin

class Article_Cosmetology(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=5500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)
	
    def __str__(self):      
        return self.title

class Article_CosmetologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title