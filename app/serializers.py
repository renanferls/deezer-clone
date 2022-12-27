from rest_framework import serializers

from .models import album, artist, genre, track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = artist
        fields = "__all__"


class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = track
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    # artist = ArtistSerializer()
    class Meta:
        model = album
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["artist"] = ArtistSerializer(instance.artist).data
        return response


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = genre
        fields = "__all__"
