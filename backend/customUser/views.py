
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
@permission_classes([IsAuthenticated])
def get(request):
    try:
        datas = Users.objects.filter(is_deleted=False, is_superuser=False, is_artist=True)
        serializer = UserSerializer(datas, many=True)
    except:
        return Response({"detail":"No User Found"}, status=404)
    return Response(serializer.data)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request,userid):
    try:
        data = Users.objects.get(pk=userid, is_deleted=False, is_superuser=False)
        serializer = UserSerializer(data, many=False)
    except:
        return Response({"detail":"No User Found"}, status=404)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=422)
    


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
@enable_disable
def delete(request,userid):
    return {"is_deleted": True}


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@enable_disable
def restore(request,userid):
    return {"is_deleted": False}


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def disable_user(request,userid):
    return {"is_disabled": True}


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def enable_user(request,userid):
    return {"is_disabled": False}


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def enable_artist(request,userid):
    return {"is_artist": True}

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@isStaff
@enable_disable
def disable_artist(request,userid):
    return {"is_artist": False}

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@isAdmin
@enable_disable
def disable_staff(request,userid):
    return {"is_staff": False}


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@isAdmin
@enable_disable
def enable_staff(request,userid):
    return {"is_staff": True}














# @csrf_exempt
# def signin(request):
#     requestData = json.loads(request.body)
#     try:
#         data =  Users.objects.values().get(email=requestData['email'],is_deleted=False)
#         if data['password'] == requestData['password']:
#             jwt = RegenerateToken(data['id'])
#             allData ={
#                 "data": DataWithoutPass(data),
#                 "jwt" : jwt
#             }
#             response =  JsonResponse(allData, safe=False, status=200)
#             # response['accessToken'] = payload.get('accessJWT')
#             # response['refreshToken'] = payload.get('refreshJWT')
#             return response
#         else:
#             return JsonResponse({"message":"Wrong UserName/Password"}, status=400)
#     except:
#         return JsonResponse({"message":"Wrong UserName/Password"}, status=400)



# def UserSerializer(obj):
#     keys = ["id", "email", "fname", "bio", "link", "gender", "img_src", "modified_by", "total_follower",  "total_music", "total_album", "is_deleted", "is_disabled", "is_artist", "is_superuser", "is_active"]
#     values = [obj.id, obj.email, obj.fname, obj.bio, obj.link, obj.gender, obj.img_src, obj.modified_by, obj.total_music , obj.total_album , obj.is_deleted , obj.is_disabled , obj.is_artist, obj.is_superuser, obj.is_active ]
#     data = {k:v for k,v in zip(keys,values)}
#     return data




# def GenerateNewToken(userId):
#     access_payload={
#         'token_type':'access',
#         'jti': math.floor(time.time()  - 100),
#         'id':userId,
#         'exp': math.floor(time.time() + 10000),
#         'iat': math.floor(time.time()),
#     }
#     refresh_payload={
#         'token_type':'refresh',
#         'id':access_payload.get('jti'),
#         'exp': math.floor(time.time() + 2592000),
#         'iat': math.floor(time.time()),
#     }
#     payload={
#         "accessJWT":jwt.encode(access_payload, "mrvishope",  algorithm="HS256"),
#         "refreshJWT":jwt.encode(refresh_payload, "mrvishope",  algorithm="HS256")
#     }
#     newToken = AccessToken.objects.create(jti=access_payload.get('jti'), userid=access_payload.get('id'))
#     newToken.save()
#     return payload




# def RegenerateToken(id):

#     AccessTokenDB = AccessToken.objects.get(userid=id) 
#     access_payload={
#         'token_type':'access',
#         'jti': math.floor(time.time()  - 100),
#         'id':id,
#         'exp': math.floor(time.time() + 10000),
#         'iat': math.floor(time.time()),
#     }
#     refresh_payload={
#         'token_type':'refresh',
#         'id':access_payload.get('jti'),
#         'exp': math.floor(time.time() + 2592000),
#         'iat': math.floor(time.time()),
#     }

#     payload={
#         "accessJWT":jwt.encode(access_payload, "mrvishope",  algorithm="HS256"),
#         "refreshJWT":jwt.encode(refresh_payload, "mrvishope",  algorithm="HS256")
#     }
     
#     AccessTokenDB.jti = access_payload.get('jti')
#     AccessTokenDB.save()
#     return payload



# def RegenerateTokenFromJTI(id):
#     AccessTokenDB = AccessToken.objects.get(jti=id) 
#     access_payload={
#         'token_type':'access',
#         'jti': math.floor(time.time()  - 100),
#         'id':1,
#         'exp': math.floor(time.time() + 10000),
#         'iat': math.floor(time.time()),
#     }
#     refresh_payload={
#         'token_type':'refresh',
#         'id':access_payload.get('jti'),
#         'exp': math.floor(time.time() + 2592000),
#         'iat': math.floor(time.time()),
#     }

#     payload={
#         "accessJWT":jwt.encode(access_payload, "mrvishope",  algorithm="HS256"),
#         "refreshJWT":jwt.encode(refresh_payload, "mrvishope",  algorithm="HS256")
#     }    
#     AccessTokenDB.jti = access_payload.get('jti')
#     AccessTokenDB.save()
#     return payload


# def verify(func):
#     def wrapper(request, *args, **kwargs):
#         if request.headers.get('Authorization'):
#             try:
#                 payload = jwt.decode(request.headers.get('Authorization'), 'mrvishope', algorithms='HS256')
                
#                 responseData = func(request, payload['id'])
#                 response = {
#                         "status":200,
#                         "resData": responseData,
#                     }
#             except:
#                 if request.headers.get('RefreshToken'):
#                     try:
#                         payload = jwt.decode(request.headers.get('RefreshToken'), 'mrvishope', algorithms='HS256')
#                         response = {    
#                                 "status": 204,
#                                 "resData": RegenerateTokenFromJTI(payload['id']),
#                             }
#                     except:
#                         response = {
#                                 "status": 200,
#                                 "resData": "No Token",
#                             }
                
#                 else:   
#                     response = {
#                                 "status": 200,
#                                 "resData": "Not Authenticated",
#                             }
#         else:
#                 try:
#                     payload = jwt.decode(request.headers.get('RefreshToken'), 'mrvishope', algorithms='HS256')
#                     response = {    
#                             "status": 204,
#                             "resData": RegenerateTokenFromJTI(payload['id']),
#                         }
#                 except:
#                     response = {
#                             "status": 200,
#                             "resData": "No Token",
#                         }
#         return JsonResponse(response, safe=False, status=200)
#     return wrapper







# @csrf_exempt
# @verify
# def checkToken(request, id):
#     try:
#         data =  Users.objects.values().get(pk=id, is_deleted=False)
#         print(data)
#         datawithoutPass = DataWithoutPass(data)
#         print(datawithoutPass)
#         return datawithoutPass
#     except:
#         return "No Dataa"



# @csrf_exempt
# def checkMailAvailable(request):
#     datas = Users.objects.all()
#     available = True
#     emailId = json.loads(request.body)
#     for data in datas:
#         if data.email == emailId["checkEmailID"]:
#             available = False
#             break
#     return JsonResponse({"availability": available } , safe=False, status=200)




