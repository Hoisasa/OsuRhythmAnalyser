# Generated by Django 4.2.13 on 2024-07-25 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoService', '0003_alter_song_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('name', 'author', 'tags')},
        ),
    ]
