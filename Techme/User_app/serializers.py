from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',  'email']
        extra_kwargs = {'username': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'password': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'email': {'required': True, 'allow_blank': False}}

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],  email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user