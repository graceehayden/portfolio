from django.shortcuts import render
from django.utils import timezone
from .models import Post


def index(request):
    return render(request, 'index.html', {})


def coming_soon(request):
    return render(request, 'coming_soon.html', {})


def resume(request):
    return render(request, 'resume.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
