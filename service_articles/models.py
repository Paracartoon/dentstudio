from django.db import models
from django.contrib import admin

class Cosmetology(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по косметологии'
        verbose_name_plural = 'Статьи по косметологии'
	
    def __str__(self):      
        return self.title

class CosmetologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title

class Gnatology(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по гнатологии'
        verbose_name_plural = 'Статьи по гнатологии'
	
    def __str__(self):      
        return self.title

class GnatologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title

class Terapy(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по терапии'
        verbose_name_plural = 'Статьи по терапии'
	
    def __str__(self):      
        return self.title

class TerapyAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title
		
class Ortoped(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по ортопедии'
        verbose_name_plural = 'Статьи по ортопедии'
	
    def __str__(self):      
        return self.title

class OrtopedAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title

class Ortodont(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по ортодонтии'
        verbose_name_plural = 'Статьи по ортодонтии'
	
    def __str__(self):      
        return self.title

class OrtodontAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title

class Hygiene(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по профгигиене'
        verbose_name_plural = 'Статьи по профгигиене'
	
    def __str__(self):      
        return self.title

class HygieneAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title
		
class Implant(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по имплантологии'
        verbose_name_plural = 'Статьи по имплантологии'
	
    def __str__(self):      
        return self.title

class ImplantAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title
		
class Parodontology(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=555500, blank=True)
    date = models.DateField(max_length=128, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=200, blank = True)
    link = models.CharField(max_length=128, blank=True)

	
    class Meta:
        verbose_name = 'Статью по пародонтологии'
        verbose_name_plural = 'Статьи по пародонтологии'
	
    def __str__(self):      
        return self.title

class ParodontologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'image', 'link')
	
    def __str__(self):     
        return self.title