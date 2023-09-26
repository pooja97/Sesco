from django.shortcuts import render

from ..models  import reactor_unit
from ..serializers.reactor_serializer import reactor_serializer
from rest_framework import generics
import django_filters.rest_framework


#Create your views here

#Script for reading report data
# with open('/Users/sheshmani/Desktop/SESCO/NRC/us_nrc/report_data.txt','r') as f:
#     report_data = f.readlines()[1:-1]
#     for line in report_data:
#         data_lst = line.split('|')
#         b =  unit_report(ReportDt = data_lst[0],Unit = data_lst[1],Power = data_lst[2])
#         b.save()
        
class reactorState(generics.ListAPIView):
    model = reactor_unit
    serializer_class = reactor_serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['State']

    def get_queryset(self):
        queryset = reactor_unit.objects.all()
        return queryset
    







