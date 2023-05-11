# Generated by Django 4.1.7 on 2023-04-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='актори', to='films.actor'),
        ),
        migrations.DeleteModel(
            name='ActorName',
        ),
    ]
