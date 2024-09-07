from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:song_id>/', views.play_song, name='play_song'),
    path('songs/', views.song_details, name='song_details'),
]