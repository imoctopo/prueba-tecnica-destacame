from django.utils import timezone
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
    schedule = serializers.SerializerMethodField('get_schedule')

    class Meta:
        model = Ride
        fields = '__all__'
        depth = 2

    def __init__(self, *args, **kwargs):
        # Remove field in nested serializers (must remove parent, e.g. routes/1/rides -> remove routes)
        remove_fields = kwargs.pop('remove_fields', list())
        super(RideDetailSerializer, self).__init__(*args, **kwargs)
        for field in remove_fields:
            self.fields.pop(field)

    @staticmethod
    def get_schedule(obj):
        return timezone.localtime(obj.schedule).strftime('%Y-%m-%dT%H:%M')
