from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path('post_list', views.post_list, name='post_list'),
    path('hello_pallet', views.hello_pallet, name='hello_pallet'),
] + staticfiles_urlpatterns()
