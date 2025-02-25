from rest_framework.permissions import BasePermission
from api1 import models
import  random
class UserPermission(BasePermission):
    message={"statue":False,"msg":"认证失败，无权访问--用户"}
    def has_permission(self, request, view):
        if request.user.role ==1:
            return True
        return False
class ManagePermission(BasePermission):
    message={"statue":False,"msg":"认证失败，无权访问--管理员"}
    def has_permission(self, request, view):
        if request.user.role ==2:
            return True
        return False

class AdminPermission(BasePermission):
    message = {"statue": False, "msg": "认证失败，无权访问--Admin"}
    def has_permission(self, request, view):
        if request.user.role == 3:
            return True
        return False