from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.index, name='index'),
    path("movie/detail/<int:pk>/", views.movies1, name="movies"),
    path("search/", views.Search.as_view(), name='search'),
    path("movies/add-movie", views.add_movie, name='add-movie')

]
