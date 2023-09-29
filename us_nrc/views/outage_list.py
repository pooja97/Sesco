# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from ..models import Report_data,reactor_unit
# from ..serializers import report_serializer.report_serializer,
from ..serializers import report_serializers

class ReactorOutageView(APIView):
    def post(self, request, *args, **kwargs):
        # Get start and end dates from user input
        start_date = datetime.datetime.strptime(self.request.data.get('start_date'),"%m/%d/%Y").date()
        end_date = datetime.datetime.strptime(self.request.data.get('end_date'),"%m/%d/%Y").date()

        if not start_date or not end_date:
            return Response({'error': 'Please provide both start_date and end_date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Report_data.objects.filter(ReportDt__range=[start_date,end_date],Power = 0).select_related("reactor")
        serializer = report_serializers.report_serializer(queryset,many=True)

        name_list = list()
        for name in serializer.data:
            name_list.append(name["Unit"])

        return Response(name_list)
