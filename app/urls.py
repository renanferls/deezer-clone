from django.urls import path

from .views import (
    CustomSearch,
    album_ListCreate,
    album_ReadUpdateDelete,
    artist_ListCreate,
    artist_ReadUpdateDelete,
    genre_ListCreate,
    genre_ReadUpdateDelete,
    queryAlbum,
    queryArtist,
    track_ListCreate,
    track_ReadUpdateDelete,
)

urlpatterns = [
    path("artist", artist_ListCreate.as_view()),
    path("artist/<int:pk>", artist_ReadUpdateDelete.as_view()),
    path("album", album_ListCreate.as_view()),
    path("album/<int:pk>", album_ReadUpdateDelete.as_view()),
    path("genre", genre_ListCreate.as_view()),
    path("genre/<int:pk>", genre_ReadUpdateDelete.as_view()),
    path("track", track_ListCreate.as_view()),
    path("track/<int:pk>", track_ReadUpdateDelete.as_view()),
    path("process/album/<int:pk>", queryAlbum.as_view()),
    path("process/artist/<int:pk>", queryArtist.as_view()),
    path("search/", CustomSearch.as_view()),
]
