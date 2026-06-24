from django.urls import path, include
from .views import MovieListView, MovieDetailView, ProducerDetailView

urlpatterns = [
    path("", MovieListView.as_view(), name="movie-list"),
    path("producers/<int:pk>/", ProducerDetailView.as_view(), name="producer-detail"),
    path("<int:pk>/", include([
        path("details/", MovieDetailView.as_view(), name="movie-detail"),
    ])),

]