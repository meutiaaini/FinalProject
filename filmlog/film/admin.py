from django.contrib import admin
from .models import Film, Genre, Review

class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres',)  

admin.site.register(Film, FilmAdmin)
admin.site.register(Genre)
admin.site.register(Review)
