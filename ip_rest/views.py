from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from .models import IpAddr
from .serializers import IpAddrSerializer


class IpAddrViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = IpAddr.objects.all()
    serializer_class = IpAddrSerializer

    def list(self, request, *args, **kwargs):
        return Response(IpAddrSerializer(IpAddr.objects.all(), many=True).data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        ip = get_object_or_404(IpAddr, id=kwargs.get('pk'))
        return Response(IpAddrSerializer(ip).data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        ip_ser = IpAddrSerializer(data=request.data)
        if ip_ser.is_valid():
            ip_ser.save()
            return Response(ip_ser.data, status=HTTP_201_CREATED)
        else:
            return Response(ip_ser.errors, status=HTTP_403_FORBIDDEN)

    @action(methods=['PUT'], detail=True, url_path='acquire')
    def acquire(self, request, *args, **kwargs):
        ip = get_object_or_404(IpAddr, id=kwargs.get('pk'))
        return IpAddrViewSet.__change_status(ip, 'acquired')

    @action(methods=['PUT'], detail=True, url_path='release')
    def release(self, request, *args, **kwargs):
        ip = get_object_or_404(IpAddr, id=kwargs.get('pk'))
        return IpAddrViewSet.__change_status(ip, 'available')

    def __change_status(ip, status):
        ip_ser = IpAddrSerializer(ip, data={'status': status, 'cidr': ip.cidr})
        if ip_ser.is_valid():
            ip_ser.save()
            return Response(ip_ser.data, status=HTTP_200_OK)
        else:
            return Response(ip_ser.errors, status=HTTP_403_FORBIDDEN)
