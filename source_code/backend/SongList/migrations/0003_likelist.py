# Generated by Django 4.2 on 2023-05-02 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('Song', '0003_alter_song_uploader'),
        ('SongList', '0002_alter_songlist_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='likeList',
            fields=[
                ('cover', models.ImageField(default='', upload_to='', verbose_name='cover')),
                ('creator', models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tag1', models.CharField(default='', max_length=30, verbose_name='tag1')),
                ('tag2', models.CharField(default='', max_length=30, verbose_name='tag2')),
                ('tag3', models.CharField(default='', max_length=30, verbose_name='tag3')),
                ('tag4', models.CharField(default='', max_length=30, verbose_name='tag4')),
                ('tag5', models.CharField(default='', max_length=30, verbose_name='tag5')),
                ('tag6', models.CharField(default='', max_length=30, verbose_name='tag6')),
                ('content', models.ManyToManyField(default=None, to='Song.song')),
            ],
        ),
    ]
