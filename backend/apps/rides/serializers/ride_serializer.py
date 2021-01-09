from rest_framework import serializers
from ..models import Ride


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'


class RideDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        depth = 2
