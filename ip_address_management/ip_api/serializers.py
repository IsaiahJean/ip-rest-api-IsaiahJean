from rest_framework import serializers
from .models import IpAddress


class IpAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAddress
        fields = '__all__'
        read_only_fields = ('ip_address','status',)