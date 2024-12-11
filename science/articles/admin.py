from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'reason', 'created_at')  # Поля, отображаемые в списке
    search_fields = ('article__title', 'user__username', 'reason')  # Поля для поиска
    list_filter = ('created_at',)  # Фильтры для удобства навигации
