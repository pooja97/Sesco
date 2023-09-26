from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from ..models  import reactor_unit
from ..serializers.reactor_serializer import reactor_serializer
from rest_framework import generics
import django_filters.rest_framework


class reactorName(generics.ListAPIView):
    model = reactor_unit
    serializer_class = reactor_serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['PlantName']

    def get_queryset(self):
        queryset = reactor_unit.objects.all()
        return queryset
