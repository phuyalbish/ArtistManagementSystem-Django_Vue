from django.urls import  path
from customUser import views



urlpatterns = [
    # Token
    # path('signin/', views.signin, name='signin'),
    # path('checkToken/', views.checkToken,  name='checkToken'),
    # path('checkMailAvailable/', views.checkMailAvailable, name="checkMail"),
    # path('user/register/', views.post, name="register"),
    path('getCSRFToken/', views.getCSRFToken ),


    # User CRUD
    path('user/get/', views.get, name="get"),
    path('user/get/<int:userid>/', views.getUser, name="getUser"),
    path('user/add/', views.add, name="add"),
    path('user/edit/<int:userid>/', views.edit, name="edit"),
    path('user/delete/<int:userid>/', views.delete, name="delete"),
    path('user/restore/<int:userid>/', views.restore, name="restore"),
    path('user/enable_user/<int:userid>/', views.enable_user, name="enable_user"),
    path('user/disable_user/<int:userid>/', views.disable_user, name="disable_user"),
    path('user/enable_artist/<int:userid>/', views.enable_artist, name="enable_artist"),
    path('user/disable_artist/<int:userid>/', views.disable_artist, name="disable_artist"),
    path('user/enable_staff/<int:userid>/', views.enable_staff, name="enable_staff"),
    path('user/disable_staff/<int:userid>/', views.disable_staff, name="disable_staff"),

   ]