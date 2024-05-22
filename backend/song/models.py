from django.db import models
from customUser.models import Users
from album.models import Album
class Song(models.Model):
    name=models.CharField(max_length=50, null=False)
    img_src=models.CharField(max_length=100, null="default_album.png")
    artist=models.OneToOneField(Users, on_delete=models.CASCADE)
    album=models.OneToOneField(Album, on_delete=models.CASCADE)
    is_hidden=models.BooleanField(default=False)
    totallikes = models.IntegerField(default=0)

