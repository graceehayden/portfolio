from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path('function_junction', views.function_junction, name='function_junction'),
    path('post_list', views.post_list, name='post_list'),
    path('resume', views.resume, name='resume'),
    path('hello_pallet', views.hello_pallet, name='hello_pallet'),
    path('palindromes', views.palindromes, name='palindromes')
] + staticfiles_urlpatterns()
