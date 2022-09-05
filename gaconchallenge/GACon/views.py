from django.shortcuts import render
from .serializers import EventSerializer, TalksSerializer, AttendeeSerializer
from .models import Talks, Event, Attendees, Speaker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EventList(APIView):

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class TalkList(APIView):

    def get(self, request, format=None):
        talks = Talks.objects.all()
        serializers = TalksSerializer(talks, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = TalksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)