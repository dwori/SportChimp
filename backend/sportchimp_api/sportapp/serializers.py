from rest_framework import serializers

from . import models
from django.contrib.auth.models import User


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sport
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_joined')


class ActivitySerializer(serializers.ModelSerializer):
    sport_genre = SportSerializer()
    created_by_user = UserSerializer()
    participants = UserSerializer(many=True)

    class Meta:
        model = models.Activity
        fields = '__all__'


class ActivitySerializer2(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model = models.Activity
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    created_by_user = UserSerializer()
    class Meta:
        model = models.Comment
        fields = '__all__'
