from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path('resume', views.resume, name='resume'),
    path('function_junction/', views.function_junction, name='function_junction'),
    path('function_junction/palindromes', views.palindromes, name='palindromes'),
    path('function_junction/post_list', views.post_list, name='post_list'),
    path('function_junction/merge_and_sort_lists', views.merge_and_sort_lists, name='merge_and_sort_lists'),    
    path('hello_pallet', views.hello_pallet, name='hello_pallet'),
] + staticfiles_urlpatterns()
