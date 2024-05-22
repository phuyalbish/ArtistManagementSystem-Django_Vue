from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Users
        
        # fields = ["email", "fname", "bio", "link", "gender", "img_src", "total_follower", "total_music", "total_album", "is_deleted", "is_disabled", "is_artist", "is_superuser"]
        fields = "__all__"
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user