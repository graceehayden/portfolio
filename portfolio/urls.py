from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path('index', views.index, name='index'),    
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('inspiration_station', views.inspiration_station, name='inspiration_station'),
    path('videos', views.videos, name='videos'),
    path('travel_inspiration', views.travel_inspiration, name='travel_inspiration'),
    path('function_junction/', views.function_junction, name='function_junction'),
    path('function_junction/palindromes', views.palindromes, name='palindromes'),
    path('function_junction/post_list', views.post_list, name='post_list'),
    path('function_junction/merge_and_sort_lists', views.merge_and_sort_lists, name='merge_and_sort_lists'),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
