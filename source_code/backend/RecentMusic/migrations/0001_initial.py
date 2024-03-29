# Generated by Django 4.2 on 2023-05-25 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_remove_user_icon_user_has_icon'),
        ('Song', '0009_alter_song_played'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayHistoryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_time', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Song.song')),
            ],
        ),
        migrations.CreateModel(
            name='PlayHistoryList',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('content', models.ManyToManyField(default=None, to='RecentMusic.playhistoryentry')),
            ],
        ),
    ]
