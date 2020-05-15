from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path('post_list', views.post_list, name='post_list'),
]
