from django.contrib.auth.models import User, Group
from .models import Award, Member
from rest_framework import serializers

class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = ('rank', 'competition', 'institution', 'participant', 'year')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('role', 'division', 'name', 'email', 'linkedin', 'photo')
