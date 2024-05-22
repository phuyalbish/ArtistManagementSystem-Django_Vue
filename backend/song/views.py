from django.shortcuts import render

import json
from .models import Users
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from song.models  import Song



def SongSerializer(obj):
    keys = ["id","name", "img_src", "artist", "album", "totallikes"]
    values = [obj.id, obj.name, obj.email, obj.img_src, obj.artist, obj.album, obj.totallikes]
    data = {k:v for k,v in zip(keys,values)}
    return data

@csrf_exempt
def post(request):
    requestData = json.loads(request.body)
    try:
        Song.objects.create(**requestData)
    except: 
            return JsonResponse({"message": "Couldn't Create Song"}, status=400)
    return JsonResponse(requestData, status=200)




def get(request):
    datas = list(Song.objects.values().filter(is_hidden=False))
    
    if datas == []:
        return JsonResponse({"message":"No Songs Found"}, status=404)
    return JsonResponse({"data":datas}, status=200)

def getSong(request, **kwargs):
    try:
        song = Song.objects.values().get(pk=kwargs.get("id"), is_hidden=False)
        return JsonResponse(song, status=200)
    except:
        return JsonResponse({"message":"No User Found"}, status=404)



@csrf_exempt
def patch(request, **kwargs):
    try:
        id = kwargs["id"]
        data = json.loads(request.body)
        updatesong = Song.objects.get(pk=id)
        updatesong.__dict__.update(data)
        updatesong.save()
       

        return JsonResponse({
                    "data": updatesong,
                    "message": "Song Updated"
                }, safe=False, status=200)
    except:
        return JsonResponse({"message":"Couldn't Edit Song"}, status=409)



@csrf_exempt
def delete(request, **kwargs):
    try:
        updatesong = Song.objects.get(pk=kwargs["id"])
        updatesong.is_deleted = True
        updatesong.save()
        data = SongSerializer(updatesong)
    except Song.DoesNotExist:
        return JsonResponse({"message": "Song not found"}, status=404)
    except Exception as e:
        return JsonResponse({"message": "Couldn't delete Song"}, status=400)
    return JsonResponse({"data": data, "message": "Song deleted"}, status=200)



@csrf_exempt
def restore(request, **kwargs):
    try:
        updatesong = Song.objects.get(pk=kwargs["id"])
        updatesong.is_deleted = False
        updatesong.save()
        data = SongSerializer(updatesong)
    except Users.DoesNotExist:
        return JsonResponse({"message": "Song not found"}, status=404)
    except Exception as e:
        return JsonResponse({"message": "Couldn't restore Song"}, status=400)
    return JsonResponse({"data": data, "message": "Song restore"}, status=200)






