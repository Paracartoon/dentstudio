from django.contrib import admin
from works.models import Work, WorkImage

class WorkImageAdmin(admin.ModelAdmin):
  pass

class WorkImageInline(admin.StackedInline):
  model = WorkImage
  max_num=20
  extra=0

class WorkAdmin(admin.ModelAdmin):
  inlines = [WorkImageInline,]


admin.site.register(Work, WorkAdmin)