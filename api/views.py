from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from .serializers import MyMemoSerializer, MyMemoToggleFavouriteSerializer
from mymemo.models import MyMemo


# Create your views here.
class MyMemoListCreate(generics.ListCreateAPIView):
    serializer_class = MyMemoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return MyMemo.objects.filter(user=user).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyMemoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyMemoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return MyMemo.objects.filter(user=user)

class MyMemoToggleFavourite(generics.UpdateAPIView):
    serializer_class = MyMemoToggleFavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return MyMemo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.favourite = not(serializer.instance.favourite)
        serializer.save()

class UserSignup(generics.GenericAPIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )

            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error': 'username taken. Choose another username'},
                status=400
            )


class UserLogin(generics.GenericAPIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        user = authenticate(
            request, username=data['username'], password=data['password']
        )
        if user is None:
            return JsonResponse(
                {'error': 'Invalid username or password!'},
                status=401
            )
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return JsonResponse({'token': str(token)}, status=200)
