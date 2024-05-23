from django.db import models
from customUser.models import Users
from album.models import Album
class Music(models.Model):
    name=models.CharField(max_length=50, null=False)
    img_src=models.CharField(max_length=100, null="default_album.png")
    artist=models.ForeignKey(Users, on_delete=models.CASCADE)
    album=models.ForeignKey(Album, null=True, on_delete=models.CASCADE)
    is_hidden=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)
    is_disabled=models.BooleanField(default=False)
    totallikes = models.IntegerField(default=0)
    modified_by=models.CharField(max_length=50, null=True)


    def __str__(self):  
     return self.name