from django.urls import path
from . import views, user_views


urlpatterns = [
    path('mymemos/', views.MyMemoListCreate.as_view()),
    path('mymemos/<int:pk>/', views.MyMemoRetrieveUpdateDestroy.as_view()),
    path('mymemos/<int:pk>/favourite/', views.MyMemoToggleFavourite.as_view()),
    path('users/signup/', user_views.UserSignup.as_view()),
    path('users/login/', user_views.UserLogin.as_view()),
    path('users/logout/', user_views.UserLogout.as_view()),
]
