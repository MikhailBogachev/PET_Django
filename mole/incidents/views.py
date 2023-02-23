from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Category, App


def index(request):
    template = 'incidents/index.html'
    cat_count = Category.objects.annotate(count=Count('app'))
    context = {
        'cat_count': cat_count
    }
    return render(request, template, context=context)

def category_list(request, category_id):
    template = 'incidents/category_list.html'
    apps = App.objects.filter(category=category_id)
    context = {
        'apps': apps
    }
    return render(request, template, context=context)
