from django.shortcuts import render, get_object_or_404, get_list_or_404
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
    apps = get_list_or_404(App, category=category_id)
    context = {
        'apps': apps
    }
    return render(request, template, context=context)

def app_detail(request, app_id):
    template = 'incidents/app_detail.html'
    app = get_object_or_404(App, pk=app_id)
    context = {
        'app': app
    }
    return render(request, template, context=context)