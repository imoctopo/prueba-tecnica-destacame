from rest_framework import serializers
from ..models import Driver


class DriverSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Driver
        fields = '__all__'
