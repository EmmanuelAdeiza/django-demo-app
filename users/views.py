from django.shortcuts import render
from django.contrib.auth import authenticate, login
from more_itertools import first
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *

# Create your views here.
class SignupAPIView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or email == '':
            return Response({"details": "Please provide valid email"}, status = 400)

        try:
            user = OKUser.objects.get(email=email)
            if user:
                return Response({"details": "User already exists"}, status = 400)
        except OKUser.DoesNotExist:
            myuser = OKUser.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email

            )
            
            myuser.set_password(password)
            myuser.save()
            # send email verification email
            return Response({'details': 'User successfully created'})