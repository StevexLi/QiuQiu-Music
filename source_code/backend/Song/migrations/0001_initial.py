# Generated by Django 4.2 on 2023-04-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='song_id')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('singer', models.CharField(default='Various Artists', max_length=100, verbose_name='Singer')),
                ('cover', models.ImageField(default='', upload_to='', verbose_name='Cover')),
                ('introduction', models.CharField(default='', max_length=300, verbose_name='Introduction')),
                ('lyric', models.URLField(verbose_name='Lyric')),
            ],
        ),
    ]