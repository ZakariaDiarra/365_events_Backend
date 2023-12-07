from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Event, Category, UserProfile, Reservation
from .serializers import EventSerializer, CategorySerializer, UserProfileSerializer, CustomUserDetailsSerializer, ReservationSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Event.objects.all()
        category_name = self.request.query_params.get('category', None)
        if category_name is not None:
            queryset = queryset.filter(category__name=category_name)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    serializer = CustomUserDetailsSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_profile(request, user_id):
    try:
        user_profile = UserProfile.objects.get(user_id=user_id)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
    except UserProfile.DoesNotExist:
        return Response({'error': 'UserProfile not found'}, status=404)
