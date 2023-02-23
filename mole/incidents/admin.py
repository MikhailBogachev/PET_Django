from django.contrib import admin

from .models import App, Category, Status

class AdminApp(admin.ModelAdmin):
    """Класс кастомизации модели App"""
    list_display = ('pk', 'title', 'text', 'pub_date', 'author', 'category', 'status',)
    list_editable = ('category', 'status',)
    search_fields = ('pk', 'title', 'author', 'category',)
    list_filter = ('pub_date', 'category', 'status')
    empty_value_display = '-пусто-'
    

class AdminCategory(admin.ModelAdmin):
    """Класс кастомизации модели Category"""
    list_display = ('pk', 'title', 'description',)
    search_fields = ('title',)


class AdminStatus(admin.ModelAdmin):
    """Класс кастомизации модели Category"""
    list_display = ('pk', 'name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'

admin.site.register(App, AdminApp)
admin.site.register(Category, AdminCategory)
admin.site.register(Status, AdminStatus)