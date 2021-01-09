from rest_framework import serializers
from ..models import Route
from ...common.errors_messages import INVALID_EXACT_LENGTH


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

    @staticmethod
    def validate_number(value):
        if len(value) != 3:
            raise serializers.ValidationError([INVALID_EXACT_LENGTH % 3])
        return value
