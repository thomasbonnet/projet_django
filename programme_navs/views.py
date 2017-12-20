from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Navigation

def index(request):
    return render(request, 'programme_navs/index.html')


def liste(request):
    navs = Navigation.objects.all()
    navs = serializers.serialize('json',navs)
    return JsonResponse(navs,safe=False)
