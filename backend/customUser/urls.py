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
    path('user/get/<int:id>/', views.getUser, name="getUser"),
    path('user/add/', views.add, name="add"),
    path('user/edit/<int:userid>/', views.edit, name="edit"),
    # path('user/delete/<int:id>/', views.delete, name="delete"),
    # path('user/restore/<int:id>/', views.restore, name="restore"),
    # path('user/disable/<int:id>/', views.restore, name="disable"),
    # path('user/enable/<int:id>/', views.restore, name="enable"),

   ]