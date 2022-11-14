from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {})


def coming_soon(request):
    return render(request, 'coming_soon.html', {})


def resume(request):
    return render(request, 'resume.html', {})

def error(request):
    return render(request, 'error.html', {})


def handler404(request, *args, **argv):
   response = render(request, 'error.html',
                                 context_instance=RequestContext(request))
   response.status_code = 404
   return response


# def handler500(request, *args, **argv):
#    response = render(request, 'error.html',
#                                  context_instance=RequestContext(request))
#    response.status_code = 500
#    return response
