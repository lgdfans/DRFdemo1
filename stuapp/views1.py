from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views import View
from jsonpickle import json

from stuapp.models import *


class ActorListView(View):
    def get(self, request):
        '''
        GET /actors/
        查询所有演员信息
        '''
        actors = Actor.objects.all()

        # aid = models.AutoField(primary_key=True)
        # aname = models.CharField(max_length=30)
        # age = models.PositiveIntegerField()
        # agender = models.CharField(max_length=1, choices=GENDER_ID)
        # birth_date = models.DateField()
        # photo = models.ImageField(default='', upload_to='actors/')

        actorList = []
        for actor in actors:
            actorList.append(({
                'aid': actor.aid,
                'aname': actor.aname,
                'age': actor.age,
                'agender': actor.agender,
                'birth_date': actor.birth_date,
                'photo': actor.photo if actor.photo else ''
            }))
        return JsonResponse(actorList, safe=False)

    def post(self, request):
        '''
        POST /actors/
        新增一名演员信息

        :param request:
        :return:
        '''

        str1 = request.body.decode()

        dict_str = json.loads(str1)

        # 省略请求参数的校验

        # 将请求参数存放到数据库
        actor = Actor.objects.create(
            aname=dict_str.get('aname'),
            age=dict_str.get('age'),
            agender=dict_str.get('agender'),
            birth_date=dict_str.get('birth_date')
        )
        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo if actor.photo else ''
        }, status=201)

class ActorDetailView(View):
    '''
    GET /actors/1/
    查看某个演员的信息

    '''

    def get(self, request, pk=1):
        pk = int(pk)
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo if actor.photo else ''
        })

        pass

    def put(self,request,pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)


        str1 = request.body.decode()

        dict_str = json.loads(str1)

        actor.aname = dict_str.get('aname')
        actor.age = dict_str.get('age')
        actor.save()

        return JsonResponse({
            'aid': actor.aid,
            'aname': actor.aname,
            'age': actor.age,
            'agender': actor.agender,
            'birth_date': actor.birth_date,
            'photo': actor.photo if actor.photo else ''
        })

    def delete(self,request,pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        actor.delete()

        return JsonResponse({
            'message': 'OK'
        },status=204)