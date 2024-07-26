from django.core.files.base import ContentFile
from django.shortcuts import render
from django.db import IntegrityError
from .models import Song
import os
import psycopg2
import re

# Create your views here.


DIRECTORY_PATH = 'C:/Users/Raffie/PycharmProjects/MusicTest/static/assets/Songs'

def photosStorage(request):
    return render(request, 'photos_index.html')


def scan_osu_file(item_path, file):
    osu_data = {
        'title': '',
        'artist': '',
        'tags': '',
        'BPM': 0.,
        'img_path': '',
    }
    bpm_calc = False
    with open(os.path.join(item_path, file), 'r', encoding='utf-8') as osuFile:
        for line in osuFile:
            if line.startswith('Title:'):
                osu_data['title'] = line.split(':', 1)[1].strip()
            elif line.startswith('Artist:'):
                osu_data['artist'] = line.split(':', 1)[1].strip()
            elif line.startswith('Tags:'):
                osu_data['tags'] = line.split(':', 1)[1].strip()
            elif line.startswith('0,0,'):
                osu_data['img_path'] = os.path.join(item_path, line.split(',')[2].split('"')[1])
            elif line.startswith('[TimingPoints]'):
                bpm_calc = True
            elif bpm_calc and bool(re.match(r'^[0-9-]', line)):
                if float(line.split(',')[1]) > 1:
                    osu_data['BPM'] = round( 60000/float(line.split(',')[1]) )
            elif line.startswith('[HitObjects]'):
                return osu_data


def search_osu_file(item_path):
    osu_data = {}
    for file in os.scandir(item_path):
        if file.is_file() and file.name.endswith('.osu'):
            osu_data = scan_osu_file(item_path, file)
            return osu_data


def process_files(DIRECTORY_PATH):
    counter = 0
    osu_maps = []

    # List all files and subdirectories in the main directory
    for item in os.listdir(DIRECTORY_PATH):
        item_path = os.path.join(DIRECTORY_PATH, item)
        counter += 1
        osu_data = search_osu_file(item_path)
        if osu_data['img_path']:
            with open(osu_data['img_path'], 'rb') as image_file:
                image_data = image_file.read()
            content_file = ContentFile(image_data, os.path.basename(osu_data['img_path']))
        else:
            with open('C:/Users/Raffie/PycharmProjects/MusicTest/static/assets/img/default/noted.jpg', 'rb') as image_file:
                image_data = image_file.read()
            content_file = ContentFile(image_data, os.path.basename('noted.jpg'))
        osu_map = Song(
            name=osu_data.get('title'),
            author=osu_data.get('artist'),
            lang=' ',
            genre=' ',
            tags=osu_data.get('tags'),
            bpm=osu_data.get('BPM'),
        )
        try:
            osu_map.save()
            osu_map.disk_image = content_file
            osu_map.save()
        except IntegrityError:
            print(f"({counter})ie{osu_data['title']}", end='')




def musicStorage(request):
    Song.objects.all().delete()
    process_files(DIRECTORY_PATH)
    songs = Song.objects.all
    return render(request, 'index.html', {'songs': songs})
