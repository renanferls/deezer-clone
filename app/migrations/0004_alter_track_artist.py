# Generated by Django 4.1.2 on 2022-10-28 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_album_artist_alter_album_genre_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="artist",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.artist"
            ),
        ),
    ]
