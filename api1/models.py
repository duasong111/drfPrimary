from django.db import models

# Create your models here.
class UserInfo(models.Model):
    #添加一个角色
    role=models.IntegerField(verbose_name="角色",choices=((1,"普通用户"),(2,"商家"),(3,"超级管理")),default=1)
    username=models.CharField(verbose_name="用户名",max_length=32)
    password= models.CharField(verbose_name="密码", max_length=64)
    token=models.CharField(verbose_name="TOKEN",max_length=64,null=True,blank=True)