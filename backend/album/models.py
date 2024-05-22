from django.db import models
from customUser.models import Users
class Album(models.Model):
    name=models.CharField(max_length=50, null=False)
    img_src=models.CharField(max_length=100, null="default_album.png")
    artist=models.OneToOneField(Users, on_delete=models.CASCADE)
    totalsongs = models.IntegerField(default=0)
    totallikes = models.IntegerField(default=0)

