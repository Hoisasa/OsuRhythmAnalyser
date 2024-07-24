from django.db import models


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=30, default='non specified')
    author = models.CharField(max_length=202, default='non specified')
    lang = models.CharField(max_length=20, default='none')
    genre = models.CharField(max_length=20, default='none')
    bpm = models.IntegerField()
    disk_image = models.ImageField(upload_to='disks/', default='default/noted.jpg')
