from rest_framework.serializers import ModelSerializer, ValidationError
import re
from .models import IpAddr


class IpAddrSerializer(ModelSerializer):
    class Meta:
        model = IpAddr
        fields = '__all__'

    def validate(self, data):
        regex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$"
        if not data.get('cidr') or re.search(regex, data['cidr']) is None:
            raise ValidationError('CIDR ip is not correct')
        return data
