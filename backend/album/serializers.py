from rest_framework import serializers
from .models import Album
from customUser.serializers import UserSerializer

class AlbumSerializer(serializers.ModelSerializer):
    # artist = UserSerializer()
    class Meta:
        model = Album
        fields = "__all__"