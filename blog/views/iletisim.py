from django.shortcuts import render
from django.http import HttpResponse


def iletisim(request):
    return HttpResponse('<h1>Merhabalar</h1>')