from django.shortcuts import render
from rest_framework import generics
from .models import IpAddress
from .serializers import IpAddressSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class IpList(viewsets.ModelViewSet):
    serializer_class = IpAddressSerializer
    queryset = IpAddress.objects.all()

class IpAcquire(generics.UpdateAPIView):
    serializer_class = IpAddressSerializer
    queryset = IpAddress.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "acquired"
        instance.save()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class IpAvailable(generics.UpdateAPIView):
    serializer_class = IpAddressSerializer
    queryset = IpAddress.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = "available"
        instance.save()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

