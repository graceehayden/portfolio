from django.contrib import admin
from django.urls import path, include

#handler404 = 'portfolio.views.handler404'
#handler500 = 'portfolio.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
