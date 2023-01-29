from django.shortcuts import render
from rest_framework import viewsets, generics
from accounts import serializer as user_serializers
from accounts import models as user_models
from accounts import permissions as user_permissions


class Login(generics.CreateAPIView):
    """View for login"""
    serializer_class = user_serializers.LoginSerializer


class EmployeeView(viewsets.ModelViewSet):
    """View for Employee"""
    permission_classes = (user_permissions.IsAuthenticated,)
    serializer_class = user_serializers.EmployeeSerializer
    queryset = user_models.Employee.objects.all()
