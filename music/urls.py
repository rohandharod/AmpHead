from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('songs', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('listenlater', views.listenlater, name='listenlater'),
    path('history', views.history, name='history'),
    path('c/<str:channel>', views.channel, name='channel'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('songs/acoustics', views.acoustics, name='acoustics'),
    path('songs/old_days', views.old_days, name='old_days'),
    path('songs/bangers', views.bangers, name='bangers'),
    path('songs/bollywood', views.bollywood, name='bollywood'),
    path('songs/country', views.country, name='country'),   
    path('delete_song', views.delete_song, name='delete_song'),
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="music/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="music/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="music/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="music/password_reset_done.html"), 
        name="password_reset_complete"),
    # path('songpost', views.songpost, name='songpost'),
    #path('watchlater', views.watchlater, name='watchlater')

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)