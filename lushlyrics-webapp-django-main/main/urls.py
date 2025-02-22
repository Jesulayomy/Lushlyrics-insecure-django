from django.urls import path

from . import views


urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),
    path("login/", views.login_user, name='login_user'),
    path("logout/", views.logout_user, name='logout_user'),
    path("signup/", views.signup, name='signup'),
    path("reset/", views.reset, name='reset'),
]
