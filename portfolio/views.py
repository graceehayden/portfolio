from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Post
from django.template import RequestContext
from .functions import *


def coming_soon(request):
    return render(request, 'coming_soon.html', {})


def hello_pallet(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'hello_pallet.html', {'posts': posts})


def resume(request):
    return render(request, 'resume.html', {})


def palindromes(request):
    answer = ''
    if 'submit' in request.GET:
        answer = check_if_palindrome(request.GET.get('word', ''))

    return render(request, 'palindromes.html', {'answer': answer})


def function_junction(request):
    return render(request, 'function_junction.html', {})

def error(request):
    return render(request, 'error.html', {})


#def handler404(request, *args, **argv):
#    response = render_to_response('error.html', {},
#                                  context_instance=RequestContext(request))
#    response.status_code = 404
#    return response


# def handler500(request, *args, **argv):
#    response = render_to_response('error.html', {},
#                                  context_instance=RequestContext(request))
#    response.status_code = 500
#    return response

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
