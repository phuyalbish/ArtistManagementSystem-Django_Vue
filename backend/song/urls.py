from django.urls import  path
from song import views



urlpatterns = [

    # Song CRUD
    path('song/get/', views.get, name="get"),
    path('song/post/', views.post, name="add"),
    path('song/get/<int:id>/', views.getSong, name="getUser"),
    path('song/edit/<int:id>/', views.patch, name="patch"),
    path('song/delete/<int:id>/', views.delete, name="delete"),
    path('song/restore/<int:id>/', views.restore, name="restore"),
   ]