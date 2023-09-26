from rest_framework import serializers
from ..models import unit_report


class report_serializer(serializers.ModelSerializer):
    class Meta:
        model = unit_report
        fields = ["id", "ReportDt", "Unit", "Power"]

