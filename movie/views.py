from django.shortcuts import render, get_object_or_404, redirect
from movie.models import Movie
from actor.models import Actor
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from .forms import MovieForm

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    paginator = Paginator(movies, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/movie/movies.html', {'movies': page_obj, 'actors': actors})


def movies1(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, '../templates/movie/detail.html', {"movie": movie})


class Search(ListView):
    model = Movie
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("Q")
        object_list = Movie.objects.filter(
            Q(name__icontains=query) | Q(year__icontains=query)
        )
        return object_list


def add_movie(request):
    movie_form = MovieForm
    if request.method == "POST":
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save()
            return redirect(index)
    return render(request, "../templates/movie/add-movie.html", {"movie_form": movie_form})


