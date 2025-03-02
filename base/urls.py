from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.registerpage, name="register"),
    path('', views.Home, name="home" ),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userprofile, name="profile"),
    path('create-room/', views.createroom, name="create-room"),
    path('update-room/<str:pk>', views.updateroom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteroom, name="delete-room"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),
    path('updateuser/', views.UpdateUser, name="updateuser"),
    path('topicspage/', views.topicspage, name="topicspage"),
    path('activitypage/', views.activitypage, name="activitypage"),
   
]