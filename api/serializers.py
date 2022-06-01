from statistics import mode
from rest_framework import serializers
from mymemo.models import MyMemo


class MyMemoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    favourite = serializers.ReadOnlyField()

    class Meta:
        model = MyMemo
        fields = ['id', 'title', 'memo', 'created', 'favourite']

class MyMemoToggleFavouriteSerializer(serializers.ModelSerializer):
    favourite = serializers.ReadOnlyField()

    class Meta:
        model = MyMemo
        fields = ['id', 'favourite']
