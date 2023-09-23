from django.shortcuts import render
from django.http import HttpResponse
from   .models  import unit_report 
# Create your views here.

def index(request):
    return HttpResponse("Initial View")


with open('/Users/sheshmani/Desktop/SESCO/NRC/us_nrc/report_data.txt','r') as f:
    report_data = f.readlines()[1:-1]
    for line in report_data:
        data_lst = line.split('|')
        b =  unit_report(ReportDt = data_lst[0],Unit = data_lst[1],Power = data_lst[2])
        b.save()
        
