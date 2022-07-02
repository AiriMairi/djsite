from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения testapp')


def categories(request, testid):
    return HttpResponse(f'<h1>Python</h1><p>{testid}</p>')
