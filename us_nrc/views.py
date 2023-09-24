from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from .models  import reactor_unit,unit_report 
from .serializers import reactor_serializer
from rest_framework import generics
import django_filters.rest_framework


#Create your views here

# with open('/Users/sheshmani/Desktop/SESCO/NRC/us_nrc/report_data.txt','r') as f:
#     report_data = f.readlines()[1:-1]
#     for line in report_data:
#         data_lst = line.split('|')
#         b =  unit_report(ReportDt = data_lst[0],Unit = data_lst[1],Power = data_lst[2])
#         b.save()
        

# @api_view(['GET'])
# def reactor_data(request):
#     reactors = reactor_unit.objects.all()
#     reactor_serial = reactor_serializer(reactors,many=True)
#     return JsonResponse({'reactors':reactor_serial.data})
    
# @api_view(['POST'])
# def reactor_post(request):
#     serializer = reactor_serializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class reactorList(generics.ListAPIView):
    model = reactor_unit
    serializer_class = reactor_serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['State']



    def get_queryset(self):
        queryset = reactor_unit.objects.all()
        return queryset






