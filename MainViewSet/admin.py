from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class AdinMovie(admin.ModelAdmin):
    list_display = ['title']