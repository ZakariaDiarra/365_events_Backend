

from rest_framework import serializers
from .models import Event
from .models import Category
from .models import UserProfile
from .models import Reservation
from django.contrib.auth.models import User

from djoser.serializers import UserSerializer as BaseUserSerializer



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'category', 'imageUrl']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SimpleEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'imageUrl']

class ReservationSerializer(serializers.ModelSerializer):
    event = SimpleEventSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'event', 'user', 'tickets']


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'birthday', 'reservations']


class CustomUserDetailsSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer):
        model = User
        fields = ['id', 'username', 'email']


