from django.shortcuts import render
from django.http import HttpResponse

def HelloWorld(request):
    return HttpResponse("<h4>Hello world/Проверка работы</h4>")