from django.shortcuts import render
from .models import Song
# Create your views here.


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def play_song(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'music/play_song.html', {'song': song})

def home(request):
    return render(request, 'music/home.html')

def song_details(request):
    return render(request, 'music/song_details.html')