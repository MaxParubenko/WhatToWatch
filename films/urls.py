from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('movie/<slug:slug>/',views.movie_page, name='movie_page'),
    path('actor/<slug:slug>/',views.actor_page, name='actor_page'),
    path('director/<slug:slug>/',views.director_page, name='director_page'),
    path('genre/<slug:slug>/',views.genre_page, name='genre_page'),
    path('/search/', views.search, name='search'),
    path('watchlist/<slug:slug>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('/watchlist/', views.watchlist, name='watchlist'),
    path('remove-from-watchlist/<slug:slug>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('/profile/', views.profile, name='profile'),
]
