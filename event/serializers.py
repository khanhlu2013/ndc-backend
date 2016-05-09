from rest_framework import serializers,fields
from event.models import Event,Venue,Attendance,Event_rate,Default_rate
from member.serializers import Member_serializer

class Venue_serializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

class Default_rate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Default_rate
        fields = ('id','rate_type','rate_amount')

class Event_rate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Event_rate
        fields = ('id','rate_type','rate_amount')

class Attendance_serializer(serializers.ModelSerializer):
    member = Member_serializer(many=False)


    class Meta:
        model = Attendance
        fields = ('id','date_time','member','anonymous_first_name','anonymous_last_name','payment_type','rate_type','rate_amount')

class Event_serializer(serializers.ModelSerializer):
    venue = Venue_serializer(many=False)
    attendance_lst = Attendance_serializer(many=True)
    event_rate_lst = Event_rate_serializer(many=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'date',
            'venue',
            'attendance_lst',
            'event_rate_lst'
        )