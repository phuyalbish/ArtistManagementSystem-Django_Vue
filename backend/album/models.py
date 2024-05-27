from django.db import models
from customUser.models import Users
class Album(models.Model):
    name=models.CharField(max_length=50, null=False)
    img_src=models.CharField(max_length=100, null="default_album.png")
    artist=models.ForeignKey(Users, on_delete=models.CASCADE, related_name="album")
    is_hidden=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)
    is_disabled=models.BooleanField(default=False)
    modified_by=models.CharField(max_length=50, null=True)
    totallikes = models.IntegerField(default=0)

    def __str__(self):  
     return self.name