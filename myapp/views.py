from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from .serializers import *
from .models import *

def Home(request):
    return HttpResponse('Hellow world')

class CountryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Country.objects.all()
    serializer_class=CountrySerializer
    
    def list(self, request):
        queryset = Country.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class  LeagueViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = League.objects.all()
    serializer_class=LeagueSerializer
    
    def list(self, request):
        queryset = League.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class  CharacteristicViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Characteristic.objects.all()
    serializer_class=CharacteristicSerializer
    
    def list(self, request):
        queryset = Characteristic.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class  FootballClubViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = FootballClub.objects.all()
    serializer_class=FootballClubSerializer
    
    def list(self, request):
        queryset = FootballClub.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

