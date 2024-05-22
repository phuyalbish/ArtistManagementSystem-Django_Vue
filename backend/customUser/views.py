
import django
from .models import Users, AccessToken
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer



@api_view(['GET'])
def getCSRFToken(request):
    try:
        token = django.middleware.csrf.get_token(request)
    except:
        return Response({'detail':"Token Not Found"}, status=404)
    return Response({'token': token})


@api_view(['GET'])
def get(request):
    try:
        datas = list(Users.objects.values().filter(is_deleted=False, is_superuser=False))
        serializer = UserSerializer(datas, many=True)
    except:
        return Response({"detail":"No User Found"}, status=404)
    return Response(serializer.data)
    


@api_view(['GET'])
def getUser(request, **kwargs):
    try:
        data = Users.objects.values().get(pk=kwargs.get("id"), is_deleted=False, is_superuser=False)
        serializer = UserSerializer(data, many=False)
    except:
        return Response({"detail":"No User Found"}, status=404)
    return Response(serializer.data)




@csrf_exempt
@api_view(['POST'])
def add(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"detail":"Not Valid Input"}, status=422)
    


@csrf_exempt
@api_view(['PATCH'])
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



@csrf_exempt
@api_view(['PATCH'])
def delete(request,id):
    try:
        user = Users.objects.get(id=userid)
    except Users.DoesNotExist:
        return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    deleteData={
        "is_deleted":True
    }
    serializer = UserSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    


# @csrf_exempt
# def delete(request, **kwargs):
#     try:
#         updateuser = Users.objects.get(pk=kwargs["id"])
#         updateuser.is_deleted = True
#         updateuser.save()
#         data = UserSerializer(updateuser)
#     except Users.DoesNotExist:
#         return JsonResponse({"message": "User not found"}, status=404)
#     except Exception as e:
#         return JsonResponse({"message": "Couldn't delete data"}, status=400)
#     return JsonResponse({"data": data, "message": "User deleted"}, status=200)



# @csrf_exempt
# def restore(request, **kwargs):
#     try:
#         updateuser = Users.objects.get(pk=kwargs["id"])
#         updateuser.is_deleted = False
#         updateuser.save()
#         data = UserSerializer(updateuser)
#     except Users.DoesNotExist:
#         return JsonResponse({"message": "User not found"}, status=404)
#     except Exception as e:
#         return JsonResponse({"message":"Couldn't Restore Data"}, status=400)
#     return JsonResponse({"data": data, "message": "User Restored" }, status=200)


















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



