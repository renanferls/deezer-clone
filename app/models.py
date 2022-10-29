from django.db import models


# Create your models here.
class artist(models.Model):
    name = models.CharField("Name", max_length=50)
    link = models.URLField("Link", max_length=200)
    picture = models.CharField("Picture", max_length=200, null=True)
    is_active = models.BooleanField("Active status", default=True)
    nb_fans = models.PositiveIntegerField("Number of fans")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ("name",)

        
class genre(models.Model):
    name = models.CharField("Name", max_length=50)
    picture = models.CharField("Picture", max_length=250, null=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ("name",)

class album(models.Model):
    artist = models.ForeignKey(artist, on_delete=models.CASCADE, related_name='artist')
    title = models.CharField("Title", max_length=100)
    cover = models.CharField("Title", max_length=200)
    genre = models.ForeignKey(genre, on_delete=models.SET_NULL, null=True, related_name='genres')
    duration = models.PositiveIntegerField("Duration sec")
    available = models.BooleanField("Available", default=True)

    created_at = models.DateTimeField(auto_now_add = True)  
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Album"
        ordering = ("title",)

class track(models.Model):
    title = models.CharField("Title", max_length=150)
    explicit_lyrics = models.BooleanField("Explicit Lyrics", default=True)
    duration = models.PositiveIntegerField("Duration Sec")
    album = models.ForeignKey(album, on_delete=models.CASCADE, related_name='tracks')
    artist = models.ForeignKey(artist, on_delete=models.CASCADE, null=True, related_name='artists')
    
    created_at = models.DateTimeField(auto_now_add = True)  
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"
        ordering = ("title",)

    

