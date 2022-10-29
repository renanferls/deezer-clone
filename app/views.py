from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import album, artist, genre, track
from .serializers import (AlbumSerializer, ArtistSerializer, GenreSerializer,
                          TrackSerializer)
from .utils import to_json

"""
CRUD METHOD FOR EVERY MODEL
"""

# ARTIST VIEWS
class artist_ListCreate(ListCreateAPIView):
    """
    View to list all Artists in the database and Create new instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = artist.objects.all()
    serializer_class = ArtistSerializer


class artist_ReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete Artist instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = artist.objects.all()
    serializer_class = ArtistSerializer


# -----------------------------------------------------------

# ALBUM VIEWS
class album_ListCreate(ListCreateAPIView):
    """
    View to list all Albums in the database and Create new instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = album.objects.all()
    serializer_class = AlbumSerializer


class album_ReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete Album instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = album.objects.all()
    serializer_class = AlbumSerializer


# -----------------------------------------------------------

# GENRE VIEWS
class genre_ListCreate(ListCreateAPIView):
    """
    View to list all Genres in the database and Create new instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = genre.objects.all()
    serializer_class = GenreSerializer


class genre_ReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete Genre instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = genre.objects.all()
    serializer_class = GenreSerializer


# -----------------------------------------------------------

# TRACK VIEWS
class track_ListCreate(ListCreateAPIView):
    """
    View to list all Tracks in the database and Create new instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = track.objects.all()
    serializer_class = TrackSerializer


class track_ReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete Track instances
    * Requires token authentication.
    """

    permission_classes = [IsAuthenticated]
    queryset = track.objects.all()
    serializer_class = TrackSerializer


# -----------------------------------------------------------

# PROCESOS SOLICITADOS


class queryArtist(APIView):
    @extend_schema(request=None)
    def get(self, request, pk):
        try:
            query_artist = artist.objects.get(id=pk)
            serializer = ArtistSerializer(query_artist)
            # querying how many albums has this artist
            nb_albums = album.objects.filter(artist=pk).count()

            # append above result to response
            # Transform data
            new_data = to_json(serializer.data)
            new_data["nb_albums"] = nb_albums

            return Response(new_data)
        except artist.DoesNotExist:
            return Response(
                {"message": "artist not found"}, status=status.HTTP_404_NOT_FOUND
            )


class queryAlbum(APIView):
    @extend_schema(request=None)
    def get(self, request, pk):
        try:
            # querying album database
            query_album = album.objects.get(id=pk)
            serializer = AlbumSerializer(query_album)
            # retrieve tracks associated to this album
            tracks = track.objects.filter(album=pk)
            track_serializer = TrackSerializer(tracks, many=True)
            # append above result to response data
            # Transform data
            # new_data = to_json(serializer.data)
            # new_data["tracks_list"] = track_serializer.data

            return Response(serializer.data)
        except album.DoesNotExist:
            return Response(
                {"message": "album not found"}, status=status.HTTP_404_NOT_FOUND
            )


class CustomSearch(APIView):
    @extend_schema(
        request=None,
        parameters=[
            OpenApiParameter(name="q", description="Keyword", type=str),
        ],
    )
    def get(self, request, *args, **kwargs):

        artist_query_set = artist.objects.all()
        album_query_set = album.objects.all()
        track_query_set = track.objects.all()

        query_param = self.request.query_params.get("q")

        data = {}
        if query_param:
            # First processing - ARTISTS
            artist_query = artist_query_set.filter(name__icontains=str(query_param))
            serializer_artist = ArtistSerializer(artist_query, many=True)
            data["artists"] = serializer_artist.data

            # Second processing - Albums
            album_query = album_query_set.filter(title__icontains=str(query_param))
            serializer_album = AlbumSerializer(album_query, many=True)
            data["albums"] = serializer_album.data

            # Third processing - Albums
            track_query = track_query_set.filter(title__icontains=str(query_param))
            serializer_track = AlbumSerializer(track_query, many=True)
            data["tracks"] = serializer_track.data

        return Response({"data": data})
