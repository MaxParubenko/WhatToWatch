# Generated by Django 4.1.7 on 2023-05-08 12:45

import datetime
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0019_alter_review_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=embed_video.fields.EmbedVideoField(blank=True, verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 8, 15, 45, 34, 346503)),
        ),
    ]
