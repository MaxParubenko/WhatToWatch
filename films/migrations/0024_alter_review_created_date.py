# Generated by Django 4.1.7 on 2023-05-10 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0023_director_url_alter_review_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 13, 47, 36, 503532)),
        ),
    ]