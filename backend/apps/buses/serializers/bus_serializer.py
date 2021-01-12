from rest_framework import serializers
from ..models import Bus
from ...common.errors_messages import INVALID_EXACT_LENGTH
from ...drivers.serializers import DriverSerializer


class BusSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(required=False)

    class Meta:
        model = Bus
        fields = '__all__'

    @staticmethod
    def validate_licence_plate(value):
        if len(value) != 6:
            raise serializers.ValidationError([INVALID_EXACT_LENGTH % 6])
        return value

    def create(self, validated_data):
        driver_id = validated_data.pop('driver', {'id': None})['id']
        bus = Bus.objects.create(**validated_data, driver_id=driver_id)
        return bus

    def update(self, instance: Bus, validated_data):
        driver_id = validated_data.pop('driver')['id']
        instance.driver_id = driver_id
        instance.licence_plate = validated_data['licence_plate']
        instance.save()
        return instance

    def validate(self, attrs):
        if 'driver' in attrs:
            queryset = Bus.objects.filter(driver__id=attrs['driver']['id'])
            if instance := self.instance:
                queryset = queryset.exclude(id=instance.id)
            if queryset.exists():
                raise serializers.ValidationError({'driver': ['This driver is assigned to another bus.']})
        return attrs
