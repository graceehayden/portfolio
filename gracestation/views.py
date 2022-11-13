from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {})


def coming_soon(request):
    return render(request, 'coming_soon.html', {})


def resume(request):
    return render(request, 'resume.html', {})
