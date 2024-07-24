from django.shortcuts import render
from .models import Song
# Create your views here.


def photosStorage(request):
    return render(request, 'photos_index.html')


def musicStorage(request):
    songs = Song.objects.all
    return render(request, 'index.html', {'songs': songs})
