import django
from .models import Album
from django.views.decorators.csrf import csrf_exempt
from .serializers import AlbumSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .decorators import isArtist, isStaffOrArtist, isStaff


def enable_disable(func):
    def wrapper(request, albumid):
        try:
            user = Album.objects.get(id=albumid)
        except Album.DoesNotExist:
            return Response({"msg": "Album not found"}, status=status.HTTP_404_NOT_FOUND)
        toggledata = func(request, albumid)
        serializer = AlbumSerializer(instance=user, data=toggledata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return wrapper


@api_view(['GET'])
def get(request):
    try:
        datas = Album.objects.filter(is_deleted=False)
        # breakpoint()

        serializer = AlbumSerializer(datas, many=True)
    except:
        return Response({"detail":"No Album Found"}, status=404)
    return Response(serializer.data)
    


@api_view(['GET'])
def getAlbum(request,albumid):
    try:
        data = Album.objects.get(pk=albumid, is_deleted=False)
        serializer = AlbumSerializer(data, many=False)
    except:
        return Response({"detail":"No Album Found"}, status=404)
    return Response(serializer.data)




@api_view(['POST'])
@isArtist
def add(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=422)
    


@api_view(['PATCH'])
@isArtist
def edit(request, albumid):
    try:
        user = Album.objects.get(id=albumid)
    except Album.DoesNotExist:
        return Response({"detail": "Album not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AlbumSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@isArtist
@enable_disable
def delete(request,albumid):
    return {"is_deleted": True}


@api_view(['PATCH'])
@isArtist
@enable_disable
def restore(request,albumid):
    return {"is_deleted": False}


@api_view(['PATCH'])
@isArtist
@enable_disable
def hide_album(request,albumid):
    return {"is_hidden": True}


@api_view(['PATCH'])
@isArtist
@enable_disable
def show_album(request,albumid):
    return {"is_hidden": False}


@api_view(['PATCH'])
@isStaff
@enable_disable
def disable_album(request, albumid):
    return {"is_disabled": True}



@api_view(['PATCH'])
@isStaff
@enable_disable
def enable_album(request, albumid):
    return {"is_disabled": False}
