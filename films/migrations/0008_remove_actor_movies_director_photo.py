# Generated by Django 4.1.7 on 2023-05-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_ratingstar_alter_review_options_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.AddField(
            model_name='director',
            name='photo',
            field=models.ImageField(default=1, upload_to='directors/'),
            preserve_default=False,
        ),
    ]
