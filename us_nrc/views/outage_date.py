from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from django.db.models import Max
from ..models import Report_data,reactor_unit

class ReactorOutageDate(APIView):
    def post(self, request, *args, **kwargs):
        #Get reactor name from the user
        reactor_name= self.request.data.get('reactor')
        if not reactor_name:
            return Response("Enter a valid reactor name")
        
        latest_outage_date = Report_data.objects.filter(Unit=reactor_name, Power=0).aggregate(latest_outage_date=Max('ReportDt'))['latest_outage_date']
        reactor_details = reactor_unit.objects.filter(PlantName=reactor_name).values()


        return Response([latest_outage_date,reactor_details])
