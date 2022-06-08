from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status


class UserSignup(generics.GenericAPIView):
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )

            token = Token.objects.create(user=user)
            return JsonResponse(
                {'token': str(token)},
                status=status.HTTP_201_CREATED
            )
        except IntegrityError:
            return JsonResponse(
                {'error': 'username taken. Choose another username'},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserLogin(generics.GenericAPIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user = authenticate(
            request, username=data['username'], password=data['password']
        )
        if user is None:
            return JsonResponse(
                {'error': 'Invalid username or password!'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return JsonResponse(
            {'token': str(token)}, status=status.HTTP_200_OK
        )


class UserLogout(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return JsonResponse({}, status=status.HTTP_200_OK)
