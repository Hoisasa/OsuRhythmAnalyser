from django.db import models


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100, default='non specified')
    author = models.CharField(max_length=102, default='non specified')
    lang = models.CharField(max_length=20, default='none')
    genre = models.CharField(max_length=20, default='none')
    tags = models.TextField(default='none')
    bpm = models.IntegerField(default=10)
    disk_image = models.ImageField(upload_to='disks/', default='default/noted.jpg')

    class Meta:
        unique_together = ('name', 'author', 'tags')
