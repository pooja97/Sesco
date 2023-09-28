from rest_framework import serializers
from ..models import Report_data


class report_serializer(serializers.ModelSerializer):
    class Meta:
        model = Report_data
        fields = ["id","reactor","ReportDt","ReportTime","ReportPeriod", "Unit", "Power"]

