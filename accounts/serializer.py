from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import serializers
from accounts import models as user_models
import exceptions


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee object
    """
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        """Meta info"""
        model = user_models.Employee
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        """Overriding create methode."""
        employee = super(EmployeeSerializer, self).create(validated_data)
        employee.is_active = True
        if 'password' in validated_data.keys():
            employee.set_password(validated_data['password'])
            employee.save()
        return employee


class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        """Overriding the Create Methode"""
        validated_data['username'] = validated_data['username']
        validated_data['password'] = validated_data['password']
        user = authenticate(
            username=validated_data['username'],
            password=validated_data['password']
        )
        if not user:
            raise exceptions.AccessForbidden("Invalid credentials")
        try:
            user_models.ProjectUser.objects.get(
                username=validated_data['username'])
        except:
            raise exceptions.AccessForbidden("Invalid credentials")

        return user

    def to_representation(self, obj):
        """
        Overriding the value returned when returning the serializer
        """
        data = {
            'id': obj.id,
            'name': obj.first_name,
            'role': obj.role,
        }
        return data
