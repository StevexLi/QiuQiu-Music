# Generated by Django 4.2 on 2023-06-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0010_remove_song_audit_ok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
