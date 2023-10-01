from django.shortcuts import render

from ..models import reactor_unit
from ..serializers.reactor_serializer import reactor_serializer
from rest_framework import generics
import django_filters.rest_framework


#Create your views here
class reactorState(generics.ListAPIView):
    model = reactor_unit
    serializer_class = reactor_serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['State']

    def get_queryset(self):
        queryset = reactor_unit.objects.all()
        return queryset
    







