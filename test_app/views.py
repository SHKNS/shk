from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from test_app.models import UnionBoard
from test_app.serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = UnionBoard.objects.all() 
    serializer_class = TestSerializer