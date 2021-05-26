from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsOwner
from .serializers import (PlaceSerializer)
from ..models import Place
from rest_framework import permissions


# Create your views here.

class PlaceListAPIView(ListCreateAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)


class PlaceDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]  # todo isowner kaldır sonra
    lookup_field = 'id'

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
