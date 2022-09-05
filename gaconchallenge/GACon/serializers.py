from rest_framework import serializers
from .models import Event, BaseModel, Speaker, Talks, Attendees

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class TalksSerializer(serializers.ModelSerializer):

    speaker = SpeakerSerializer(many=True)

    def create(self, validated_data):

        speaker_data = validated_data.pop('speaker')
        talk = Talks.objects.create(**validated_data)
        for speakers in speaker_data:
            Speaker.objects.create(speaker=speakers)
        return talk

    class Meta:
        model = Talks
        fields = '__all__'

class AttendeeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        attendees = Attendees.objects.create(**validated_data)
        return attendees
    class Meta:
        model = Attendees
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    talks = TalksSerializer(many=True)
    attendees = AttendeeSerializer(many=True)
    class Meta:
        model = Event