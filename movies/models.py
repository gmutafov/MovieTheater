from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)

    @property
    def movie_count(self):
        return self.movies.count()

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = "ACTION", "Action"
        DRAMA = "DRAMA", "Drama"
        COMEDY = "COMEDY", "Comedy"
        SCIFI = "SCIFI", "Sci-Fi"
        HORROR = "HORROR", "Horror"
        
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=Genre.choices)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title
    
class CinemaHall(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.location}"
    
class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings')
    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name='screenings')
    screening_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["screening_time"]

    def __str__(self):
        return f"{self.movie.title} at {self.hall.name} on {self.screening_time}"