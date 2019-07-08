from rest_framework import serializers

from stuapp.models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    """演员序列化器"""

    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """演员序列化器"""

    class Meta:
        model = Movie
        fields = '__all__'


from rest_framework.generics import *