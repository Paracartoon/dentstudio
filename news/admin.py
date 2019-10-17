from django.contrib import admin
from news.models import New, NewAdmin

admin.site.register(New, NewAdmin)