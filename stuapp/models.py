from django.db import models

# Create your models here.
'''以一个演员可以出演多部影片为例'''


class Actor(models.Model):
    GENDER_ID = (
        ('0', '男'),
        ('1', '女'),
    )
    aid = models.AutoField(primary_key=True, verbose_name='序号')
    aname = models.CharField(max_length=30, verbose_name='姓名', help_text='请输入演员姓名')
    age = models.PositiveIntegerField(verbose_name='年龄')
    agender = models.CharField(max_length=1, verbose_name='性别', choices=GENDER_ID)
    birth_date = models.DateField(verbose_name='出生日期')
    photo = models.ImageField(default='', verbose_name='照片', upload_to='actors/')

    def __str__(self):
        return self.aname


class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=30, verbose_name='影片名称')
    m_pub_date = models.DateField(verbose_name='上映日期')
    mread = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    mcomment = models.TextField(verbose_name='评论')
    mimage = models.ImageField(upload_to='movies/', verbose_name='图片', null=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, verbose_name='演员')

    def __str__(self):
        return self.mname
