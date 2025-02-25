from rest_framework.views import APIView
#这块部分的作用就是来进行认证的时候进行或操作，只要有可以通过的都可以进行通过
class NbAPIView(APIView):
    def check_permissions(self, request):
        no_permission_objects=[]
        for permission in self.get_permissions():
            if permission.has_permission(request,self):
                return
            else:
                no_permission_objects.append(permission)
        else:
            self.permission_denied(
                request,
                message=getattr(no_permission_objects[0],'message',None),
                code=getattr(no_permission_objects[0],'code',None)
            )
