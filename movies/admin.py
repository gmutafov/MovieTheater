from django.contrib import admin

from django.contrib import admin
from .models import Producer, Actor, Movie, CinemaHall, Screening

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ("name", "movie_count")

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "producer", "release_date")
    list_filter = ("release_date", "producer")
    search_fields = ("title",)

admin.site.register(Actor)
admin.site.register(CinemaHall)
admin.site.register(Screening)