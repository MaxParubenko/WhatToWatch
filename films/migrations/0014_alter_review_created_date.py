# Generated by Django 4.1.7 on 2023-05-06 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0013_review_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 13, 22, 35, 765075)),
        ),
    ]