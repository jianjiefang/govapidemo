from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from gov.models import Gov_history
from gov.permissions import IsOwnerOrReadOnly
from gov.serializers import GovSerializer
from gov.serializers import UserSerializer, GroupSerializer


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)


class GovViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Gov_history.objects.all()
    serializer_class = GovSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#
# @csrf_exempt
# def gov_list(request):
#     """
#     列出所有的合格证信息，或者创建一个新的合格证
#     """
#     if request.method == 'GET':
#         govs = Gov_history.objects.all()
#         serializer = GovSerializer(govs, many=True)
#         return JSONResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = GovSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def gov_detail(request, pk):
#     """
#     获取，更新或删除一个gov
#     :param request:
#     :param pk:
#     :return:
#     """
#     try:
#         gov = Gov_history.objects.get(pk=pk)
#     except gov.DoesNotExist:
#         return HttpResponse('找不到对应的合格证，请输入正确的ID。', status=404)
#
#     if request.method == 'GET':
#         serializer = GovSerializer(gov)
#         return HttpResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser.parse(request)
#         serializer = GovSerializer(gov, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         gov.delete()
#         return HttpResponse(status=204)




























