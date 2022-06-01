from django.urls import path
from . import views


urlpatterns = [
    path('mymemos/', views.MyMemoListCreate.as_view()),
    path('mymemos/<int:pk>/', views.MyMemoRetrieveUpdateDestroy.as_view()),
    path('mymemos/<int:pk>/favourite/', views.MyMemoToggleFavourite.as_view()),
    path('signup/', views.UserSignup.as_view()),
    path('login/', views.UserLogin.as_view()),
]
