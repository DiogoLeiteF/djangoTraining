from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Movie, Snippets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ["name", "description"]



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippets
        fields= ["snippet"]
