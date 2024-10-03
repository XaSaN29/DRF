from .models import Menyu, Comment
from rest_framework import serializers


class MenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menyu
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class DeleteManyuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menyu
        fields = ['name', 'price', 'category']


class UpdateManyuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menyu
        fields = ['name', 'price', 'category', 'abut']