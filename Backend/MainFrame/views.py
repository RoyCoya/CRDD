from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerOnly
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Test
from .serializers import TestSerializer
from MainFrame.response import *


# Create your views here.
def homepage(request):
    return SUCCESS

class Login(APIView):
    def get(self, request):
        return client_error("不可使用get方式访问该接口")

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return success("登录成功\t Logged in",{
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return NOT_AUTHORIZED

class UserInfo(APIView):
    def get(self, request):
        return TODO

# only for test

# class TestAPIView(generics.ListAPIView):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer

class TestAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return SUCCESS
    def post(self, request):
        return SUCCESS
