from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('portfolio/', include('portfolio.urls')),
    path('personal/', include('personal.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
