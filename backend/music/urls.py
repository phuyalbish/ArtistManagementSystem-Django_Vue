from django.urls import  path
from music import views



urlpatterns = [

    # music CRUD

    path('music/get/', views.get, name="get"),
    path('music/get/<int:musicid>/', views.getUser, name="getUser"),
    path('music/add/', views.add, name="add"),
    path('music/edit/<int:musicid>/', views.edit, name="edit"),
    path('music/delete/<int:musicid>/', views.delete, name="delete"),
    path('music/restore/<int:musicid>/', views.restore, name="restore"),
    path('music/show_music/<int:musicid>/', views.hide_music, name="show_music"),
    path('music/hide_music/<int:musicid>/', views.show_music, name="hide_music"),
    path('music/disable_music/<int:musicid>/', views.disable_music, name="disable_music"),
    path('music/enable_music/<int:musicid>/', views.enable_music, name="enable_music"),
   ]

