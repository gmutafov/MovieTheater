from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Producer



class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie-list.html"
    context_object_name = "movies"
    paginate_by = 6

    def get_queryset(self):
        queryset = (
            Movie.objects
            .select_related("producer")
            .prefetch_related("actors")
        )

        q = self.request.GET.get("q")
        genre = self.request.GET.get("genre")

        if q:
            queryset = queryset.filter(title__icontains=q)

        if genre:
            queryset = queryset.filter(genre=genre)

        return queryset

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie-detail.html"
    context_object_name = "movie"

    def get_queryset(self):
        return (
            Movie.objects
            .select_related("producer")
            .prefetch_related("actors", "screenings__hall")
        )



class ProducerDetailView(DetailView):
    model = Producer
    template_name = "movies/producer-detail.html"
    context_object_name = "producer"