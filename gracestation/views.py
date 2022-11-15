from django.shortcuts import render
from django.views import View


class Index(View):
    """ Site landing page """
    def get(self, request):
        return render(request, 'index.html', {})
