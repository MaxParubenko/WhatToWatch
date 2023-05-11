from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from embed_video.fields import EmbedVideoField


class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='actors/')
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('actor_page', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Актор"
        verbose_name_plural = "Актори"


class Director(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='directors/', default=None)
    url = models.SlugField(max_length=130)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('director_page', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Режисер"
        verbose_name_plural = "Режисери"



class Genre(models.Model):
    name = models.CharField(max_length=255)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_page', kwargs={'slug': self.url})
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"



class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    year = models.PositiveSmallIntegerField("Дата выхода", default=2000)
    director = models.ManyToManyField(Director, related_name='режисер')
    actors = models.ManyToManyField(Actor, related_name='актори')
    genre = models.ManyToManyField(Genre,related_name='жанри' )
    poster = models.ImageField('Постер', upload_to='poster/')
    url = models.SlugField(max_length=130, unique=True)
    trailer = EmbedVideoField(blank=True, verbose_name='Трейлер')

    def get_absolute_url(self):
        return reverse('movie_page', kwargs={'slug': self.url})

    def __str__(self):
        return self.title

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)


    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"




class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, related_name='фільми')

    def __str__(self):
        return f'{self.user} - Потрібно подивитись'

    class Meta:
        verbose_name = "Обране"
        verbose_name_plural = "Обране"



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey(
        'self', verbose_name="Батько", on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.user} - {self.movie}'

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"



