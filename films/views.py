from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ReviewForm, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import Movie, Genre, Actor, Director, Review, WatchList
import datetime
from django.core.paginator import Paginator
from django.db.models import Q




def get_genres():
    all = Genre.objects.all()
    count = all.count()
    step = count // 4 + (count % 4 > 0)
    first_quarter = all[:step]
    second_quarter = all[step:step*2]
    third_quarter = all[step*2:step*3]
    fourth_quarter = all[step*3:]
    return {'gen1': first_quarter, 'gen2': second_quarter,'gen3': third_quarter, 'gen4': fourth_quarter}

def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'movies': page_obj, 'paginator':paginator}
    context.update(get_genres())
    return render(request, 'films/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {'form': form}
    context.update(get_genres())
    return render(request, 'registration/register.html',context )

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)
    context = {'form': form}
    context.update(get_genres())
    return render(request, 'films/profile.html', context)


def movie_page(request, slug):
    movie = get_object_or_404(Movie,url=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.created_date = datetime.datetime.now()
            if request.POST.get("parent", None):
                parent_id = int(request.POST.get("parent"))
                review.parent = Review.objects.get(id=parent_id)
            review.save()
            return redirect('movie_page', slug=movie.url)
    else:
        form = ReviewForm()
    reviews = Review.objects.filter(movie=movie)
    context = {'movie': movie, 'reviews': reviews, 'form': form}
    context.update(get_genres())
    return render(request, 'films/movie_page.html', context)


    

def actor_page(request,slug):
    actor = get_object_or_404(Actor,url=slug)
    movie = Movie.objects.filter(actors=actor)
    context = {'movie':movie, 'actor':actor}
    context.update(get_genres())
    return render(request, 'films/actor_page.html',context)


def director_page(request,slug):
    director = get_object_or_404(Director,url=slug)
    movie = Movie.objects.filter(director=director)
    context = {'movie':movie, 'director':director}
    context.update(get_genres())
    return render(request, 'films/director_page.html',context)

def genre_page(request,slug):
    genre = get_object_or_404(Genre,url=slug)
    movies = Movie.objects.filter(genre=genre).order_by()
    paginator = Paginator(movies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'movies':page_obj,'genre':genre, 'paginator':paginator}
    context.update(get_genres())
    return render(request,'films/genre_page.html',context)


def search(request):
    query = request.POST.get('query')
    movies = Movie.objects.filter(Q(title__icontains=query))
    context = {'movies': movies}
    context.update(get_genres())
    return render(request, "films/index.html", context)


@login_required
def add_to_watchlist(request, slug):
    movie = Movie.objects.get(url=slug)
    watchlist, delete= WatchList.objects.get_or_create(user=request.user)
    watchlist.movies.add(movie)
    return redirect('movie_page', slug=movie.url)


@login_required
def remove_from_watchlist(request, slug):
    movie = get_object_or_404(Movie, url=slug)
    watchlist = WatchList.objects.filter(user=request.user).first()
    if watchlist:
        watchlist.movies.remove(movie)
    return redirect('movie_page', slug=movie.url)

@login_required
def watchlist(request):
    watchlist = WatchList.objects.filter(user=request.user).first()
    movies = watchlist.movies.all() if watchlist else []
    paginator = Paginator(movies, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'watchlist': watchlist, 'movies': page_obj, 'paginator': paginator}
    context.update(get_genres())
    return render(request, 'films/watchlist.html', context)