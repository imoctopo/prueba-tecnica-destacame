from rest_framework import serializers
from ..models import Bus
from ...common.errors_messages import INVALID_EXACT_LENGTH


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

    @staticmethod
    def validate_licence_plate(value):
        if len(value) != 6:
            raise serializers.ValidationError([INVALID_EXACT_LENGTH % 6])
        return value
