# Generated by Django 4.2 on 2023-06-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SongList', '0009_songlist_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songlist',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
