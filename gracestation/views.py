from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    """ Site landing page """
    template_name = 'index.html'
