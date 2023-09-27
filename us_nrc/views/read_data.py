# from ..models import Report_data, reactor_unit
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     with open('/Users/sheshmani/Desktop/SESCO/NRC/us_nrc/report_data.txt','r') as f:
#         report_data = f.readlines()[1:-1]
#         for line in report_data:
#             data_lst = line.split('|')
#             r_id = reactor_unit.objects.all().filter(PlantName=data_lst[1]).first()
#             b =  Report_data(reactor=r_id, ReportDt = data_lst[0],Unit = data_lst[1],Power = data_lst[2])
#             b.save()
#     return HttpResponse("Done")

    
           