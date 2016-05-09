from member.models import Member
from member.serializers import Member_serializer
from rest_framework import generics


class Member_lst(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = Member_serializer

class Member_detail(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = Member_serializer
    