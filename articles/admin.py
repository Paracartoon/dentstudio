from django.contrib import admin
from articles.models import Article, ArticleAdmin

admin.site.register(Article, ArticleAdmin)