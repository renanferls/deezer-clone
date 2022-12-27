from django.contrib import admin

from .models import album, artist, genre, track

# Register your models here.

admin.site.register(artist)
admin.site.register(album)
admin.site.register(track)
admin.site.register(genre)
