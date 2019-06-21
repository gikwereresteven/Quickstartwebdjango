from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Registration



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('firstname','lastname','email','talkid','gender','borndate','password')
        