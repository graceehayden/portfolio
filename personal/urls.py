from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', views.home, name='home'),
    path('inspiration_station', views.inspiration_station, name='inspiration_station'),
    path('travel_inspiration', views.travel_inspiration, name='travel_inspiration'),
    path('videos', views.videos, name='videos'),
    path('hello_pallet', views.hello_pallet, name='hello_pallet'),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
