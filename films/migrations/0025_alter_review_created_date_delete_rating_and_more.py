# Generated by Django 4.1.7 on 2023-05-10 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0024_alter_review_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 17, 8, 13, 85698)),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
