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
