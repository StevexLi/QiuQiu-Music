# Generated by Django 4.2 on 2023-05-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0003_alter_song_uploader'),
        ('SongList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songlist',
            name='content',
            field=models.ManyToManyField(default=None, to='Song.song'),
        ),
    ]
