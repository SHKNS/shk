from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from myapp.models import Version
from myapp.serializers import VersionSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer