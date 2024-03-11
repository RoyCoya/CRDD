from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Test
from .serializers import TestSerializer

# Create your views here.
def homepage(request):
    return HttpResponse('ok')

# views.py
class TestAPIView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
