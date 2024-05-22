from django.urls import  path
from album import views



urlpatterns = [

    # album CRUD

    path('album/get/', views.get, name="get"),
    path('album/get/<int:albumid>/', views.getUser, name="getUser"),
    path('album/add/', views.add, name="add"),
    path('album/edit/<int:albumid>/', views.edit, name="edit"),
    path('album/delete/<int:albumid>/', views.delete, name="delete"),
    path('album/restore/<int:albumid>/', views.restore, name="restore"),
    path('album/show_album/<int:albumid>/', views.hide_album, name="show_album"),
    path('album/hide_album/<int:albumid>/', views.show_album, name="hide_album"),
   ]

