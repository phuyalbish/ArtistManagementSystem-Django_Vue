
import django
from .models import Users
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from .decorators import isStaff, isAdmin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView



@api_view(['GET'])
def getCSRFToken(request):
    try:
        token = django.middleware.csrf.get_token(request)
    except:
        return Response({'detail':"Token Not Found"}, status=404)
    return Response({'token': token})




def enable_disable(func):
    def wrapper(request, userid):
        try:
            user = Users.objects.get(id=userid)
        except Users.DoesNotExist:
            return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        toggledata = func(request, userid)
        serializer = UserSerializer(instance=user, data=toggledata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return wrapper


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get(request):
    try:
        datas = Users.objects.filter(is_deleted=False, is_superuser=False, is_artist=True)
        serializer = UserSerializer(datas, many=True)
    except:
        return Response({"detail":"No User Found"}, status=404)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getUser(request,userid):
    try:
        data = Users.objects.get(pk=userid, is_deleted=False)
        serializer = UserSerializer(data, many=False)
    except:
        return Response({"detail":"No User Found"}, status=404)
    return Response(serializer.data)


@api_view(['POST'])
def add(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=422)
    


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def edit(request,userid):
    try:
        user = Users.objects.get(id=userid)
    except Users.DoesNotExist:
        return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def editSuperUser(request,userid):
    try:
        user = Users.objects.get(id=userid)
    except Users.DoesNotExist:
        return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@enable_disable
def delete(request,userid):
    return {"is_deleted": True}


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@enable_disable
def restore(request,userid):
    return {"is_deleted": False}


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def disable_user(request,userid):
    return {"is_disabled": True}


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def enable_user(request,userid):
    return {"is_disabled": False}


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def enable_artist(request,userid):
    return {"is_artist": True}

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def disable_artist(request,userid):
    return {"is_artist": False}

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@isAdmin
@enable_disable
def disable_staff(request,userid):
    return {"is_staff": False}


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
@isAdmin
@enable_disable
def enable_staff(request,userid):
    return {"is_staff": True}







