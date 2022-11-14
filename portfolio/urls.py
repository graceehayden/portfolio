from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'^portfolio/$', views.portfolio, name='portfolio'),
    path('', views.portfolio, name='portfolio'),
    path('user_login', views.user_login, name='user_login'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('signout', views.signout, name="signout"),
    path('resume', views.resume, name='resume'),
    path('inspiration_station', views.inspiration_station, name='inspiration_station'),
    path('function_junction/', views.function_junction, name='function_junction'),
    path('function_junction/palindromes', views.palindromes, name='palindromes'),
    path('function_junction/merge_and_sort_lists', views.merge_and_sort_lists, name='merge_and_sort_lists'),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
