from event.models import Event,Venue
from event.serializers import Event_serializer,Venue_serializer
from rest_framework import generics


class Event_lst(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = Event_serializer

class Event_detail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = Event_serializer
    
class Venue_lst(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = Venue_serializer