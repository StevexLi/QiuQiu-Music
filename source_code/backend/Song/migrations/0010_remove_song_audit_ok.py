# Generated by Django 4.2 on 2023-06-06 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0009_alter_song_played'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audit_ok',
        ),
    ]
