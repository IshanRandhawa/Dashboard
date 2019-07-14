from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import L4, L3

def L4_page(request):
    data = L4.objects.all()
    template = loader.get_template('Viewer/l4.html')
    context = {
        'data' : data,
    }
    return HttpResponse(template.render(context, request))

def L3_page(request, f_id):
    man = L4.objects.get(pk = f_id)
    data = L3.objects.all()
    data = data.filter(manager = man)
    template = loader.get_template('Viewer/l3.html')
    context = {
        'data' : data,
    }
    return HttpResponse(template.render(context, request))