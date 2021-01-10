from rest_framework import serializers
from ..models import Ride


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        extra_kwargs = {
            'schedule': {
                'required': True
            }
        }


class RideDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        depth = 2

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', list())
        super(RideDetailSerializer, self).__init__(*args, **kwargs)
        for field in remove_fields:
            self.fields.pop(field)
