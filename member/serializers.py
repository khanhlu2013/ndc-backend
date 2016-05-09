from rest_framework import serializers,fields
from member.models import Member

class Member_serializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = (
            'id',
            'first_name',
            'last_name',
            'ndc_old_id',
            'create_date',
            'phone',
            'email'
        )