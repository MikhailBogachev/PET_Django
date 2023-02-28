from django.urls import path

from . import views

app_name = 'incidents'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.category_list, name='category_list'),
    path('app_detail/<int:app_id>', views.app_detail, name='app_detail'),
]