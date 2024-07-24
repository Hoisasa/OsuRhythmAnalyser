from django.contrib import admin
from .models import Song


class SongModelAdmin(admin.ModelAdmin):
    search_fields = ['name']


# Register your models here.
admin.site.register(Song, SongModelAdmin)
