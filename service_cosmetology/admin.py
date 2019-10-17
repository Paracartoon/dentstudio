from django.contrib import admin
from service_cosmetology.models import Article_Cosmetology, Article_CosmetologyAdmin

admin.site.register(Article_Cosmetology, Article_CosmetologyAdmin)