from rest_framework import serializers
from ..models import Ticket, Ride
from ...common.errors_messages import SEAT_TAKEN, PASSENGER_ALREADY_IN_THIS_RIDE, NO_FREE_SEATS


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        extra_kwargs = {
            'ride': {
                'required': True
            }
        }

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', list())
        super(TicketSerializer, self).__init__(*args, **kwargs)
        for field in remove_fields:
            self.fields.pop(field)

    def validate(self, attrs):
        # if not self.instance:
        ride = attrs['ride']
        passenger = attrs['passenger']
        ticket_pk = self.instance.id if self.instance else None
        if ride.tickets.all().count() >= 10:
            raise serializers.ValidationError({'ticket': [NO_FREE_SEATS]})
        if taken := ride.tickets.filter(seat=attrs['seat']).exclude(pk=ticket_pk).first():
            raise serializers.ValidationError({'seat': [SEAT_TAKEN % taken.passenger]})
        if not ticket_pk and ride.tickets.filter(passenger_id=passenger.id).exists():
            raise serializers.ValidationError({'passenger': [PASSENGER_ALREADY_IN_THIS_RIDE]})
        return attrs


class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        depth = 3

    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', list())
        super(TicketDetailSerializer, self).__init__(*args, **kwargs)
        for field in remove_fields:
            self.fields.pop(field)
