from django.shortcuts import redirect
from .models import Users
from rest_framework.response import Response

def not_auth(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request, *args, **kwargs)
    return wrapper


def isArtist(func):
    def wrapper(request, **kwargs):
        try:
            data = Users.objects.get(pk=request.headers.get('Userid'), is_deleted=False, is_superuser=False)
            if not data.is_artist:
                 return Response({'detail':"User is Not Authorized"}, status=404)
        except:
                return Response({'detail':"User Not Found"}, status=404)
        return func(request, **kwargs)       
    return wrapper

def isStaff(func):
    def wrapper(request, **kwargs):
        try:
            data = Users.objects.get(pk=request.headers.get('Userid'), is_deleted=False)
            if not data.is_staff:
                 return Response({'detail':"User is Not Authorized"}, status=404)
        except:
                return Response({'detail':"User Not Found"}, status=404)
        return func(request,**kwargs)       
    return wrapper


def isStaffOrArtist(func):
    def wrapper(request, **kwargs):
        try:
            data = Users.objects.get(pk=request.headers.get('Userid'), is_deleted=False)
            if not data.is_staff and not data.is_artist:
                 return Response({'detail':"User is Not Authorized"}, status=404)
        except:
                return Response({'detail':"User Not Found"}, status=404)
        return func(request,**kwargs)       
    return wrapper
