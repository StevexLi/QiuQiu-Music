# Generated by Django 4.2 on 2023-05-01 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Song', '0002_song_tag1_song_tag2_song_tag3_song_tag4_song_tag5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
