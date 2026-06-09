from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Morador
from .serializers import MoradorSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer