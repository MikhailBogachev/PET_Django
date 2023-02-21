from django.contrib import admin

from .models import App, Category

class AdminApp(admin.ModelAdmin):
    """Класс кастомизации модели App"""
    list_display = ('pk', 'title', 'text', 'pub_date', 'author', 'category',)
    list_editable = ('category',)
    search_fields = ('pk', 'title', 'author', 'category',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    


class AdminCategory(admin.ModelAdmin):
    """Класс кастомизации модели Category"""
    list_display = ('pk', 'title', 'description',)
    search_fields = ('title',)

admin.site.register(App, AdminApp)
admin.site.register(Category, AdminCategory)