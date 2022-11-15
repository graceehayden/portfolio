from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home', views.Home.as_view(), name='home'),
    path('upload_song', views.upload_song, name='upload_song'),
    path('playlist', views.playlist, name='playlist'),
    path('videos', views.videos, name='videos'),
    path('hello_pallet', views.hello_pallet, name='hello_pallet'),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
