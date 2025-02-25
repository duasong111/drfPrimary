from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api1 import models


class QueryParamsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if not token:
            return
        user_object = models.UserInfo.objects.filter(token=token).first()
        if user_object:
            return user_object, token
        return

    def authenticate_header(self, request):
        return "API"


class HeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return
        user_object = models.UserInfo.objects.filter(token=token).first()
        # 下边是属于认证成功可以返回值，认证失败是返回none
        if user_object:
            return user_object, token
        return

    def authenticate_header(self, request):
        return "API"


class NoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        raise AuthenticationFailed({"code": 1000, "msg": "认证失败"})

    def authenticate_header(self, request):
        return "API"
