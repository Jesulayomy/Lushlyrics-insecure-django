import django

from django.contrib import admin
from django.urls import path, include


def error_400_view(request):
    return django.views.defaults.bad_request(request, None)


def error_404_view(request):
    return django.views.defaults.page_not_found(request, None)


def error_500_view(request):
    return django.views.defaults.server_error(request, None)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include("django.contrib.auth.urls")),
    path('400/', error_400_view),
    path('404/', error_404_view),
    path('500/', error_500_view),
]
