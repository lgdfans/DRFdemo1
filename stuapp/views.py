from rest_framework.viewsets import ModelViewSet

from stuapp.models import Actor, Movie
from stuapp.serializers import ActorSerializer, MovieSerializer


class ActorView(ModelViewSet):
    """
    create:
    增加演员信息

    retrieve:
    查询某个演员信息

    all:
    查询所有演员信息

    del:
    删除操作

    update:
    修改操作
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieView(ModelViewSet):
    """
    查询所有演片信息、增加演片信息、修改、删除操作
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


