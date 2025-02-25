from rest_framework.views import APIView
from rest_framework.response import Response
from api1 import models
import uuid
from ext import code
from ext.per import UserPermission,ManagePermission,AdminPermission
from ext.view import NbAPIView
from ext.throttle import IpThrottle,UserThrottle
class LoginView(APIView):
    authentication_classes = []
    throttle_classes = [IpThrottle] #设置节流的操作
    def post(self, request):
        user=request.data.get("username")
        pwd=request.data.get("password")
        user_object=models.UserInfo.objects.filter(username=user,password=pwd).first()
        print("用户名和密码",user,pwd)

        """生成一个uuid来放到token中"""
        token=str(uuid.uuid4())
        user_object.token=token
        user_object.save()

        if not user_object:
            return Response({"code":f"{code.ERROR}", "error": "用户或密码反生错误"})
        else:
            return Response({"code":f"{code.SUCCESS}", "data": f"{token}"})
class UserView(NbAPIView):
    permission_classes = [AdminPermission]

    def get(self, request):
        print(request.user,request.auth)
        return Response("请求UserView页面成功")

class orderView(NbAPIView):
    #此时的权限值局部的，同时继承了NbAPIView现在是且的关系
    permission_classes = [UserPermission,ManagePermission,AdminPermission]
    throttle_classes = [UserThrottle]
    def get(self,request):
        result={
            "code":300,
            "msg":"这里是数据，叭叭叭",
            "data":"xxxxx"
        }
        return Response(result)

class TestView(NbAPIView):
    permission_classes = [ManagePermission, AdminPermission]
    def get(self, request):
        result = {
            "code": 200,
            "msg": "这里显示的是管理者的页面",
            "data": "xxxxx"
        }
        return Response(result)
    # def initialize_request(self, request, *args, **kwargs):
    #     # super().initialize_request()
    #     parser_context = self.get_parser_context(request)
    #     return Request(
    #         request,
    #         parsers=self.get_parsers(),
    #         authenticators=self.get_authenticators(),
    #         negotiator=self.get_content_negotiator(),
    #         parser_context=parser_context
    #     )





