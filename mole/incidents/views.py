from django.shortcuts import render, HttpResponse


def index(request):
    template = 'incidents/index.html'
    return render(request, template)