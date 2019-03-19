from rest_framework import serializers
from .models import VoterDetail


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoterDetail
        fields = '__all__'


class VotersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoterDetail
        fields = ('voter_id', 'voter_name', 'vote_time')


