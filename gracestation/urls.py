from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
    path('portfolio/', include('portfolio.urls')),
    path('personal/', include('personal.urls')),
]
