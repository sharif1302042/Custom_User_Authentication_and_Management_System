from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from user_management.forms import UserCreationForm, UserLoginForm
from user_management.models import User
from user_management.serializers import UserCreationSerializer


class UserCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration.html'

    def post(self, request):
        serializer = UserCreationSerializer(data= request.data)
        if serializer.is_valid():
            staus= serializer.save()
            if staus:
                return redirect('user/thanks/')
        form = UserCreationForm()
        msg = "Password Mismatch or User already exists"
        return Response({"form": form, "msg": msg})

    def get(self, request):
        form = UserCreationForm()
        queryset = "This is Home Page"
        return Response({'form': form})


class ThankYou(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'thank_you.html'

    def get(self, request):
        # form = UserCreationForm()
        msg = "Thank You"
        return Response({'msg': msg})


class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username,password=password)
        if user:
            print(request.user)
            return redirect('user/dashboard/')
        form = UserLoginForm()
        msg = "User Name or Password Doesnot Match"
        return Response({"msg":msg,"form":form})

    def get(self, request):
        form = UserLoginForm()
        return Response({'form': form})


class Dashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'
    def get(self,request):
        return Response()
