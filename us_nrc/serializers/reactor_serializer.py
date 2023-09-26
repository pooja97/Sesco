from rest_framework import serializers

from ..models import reactor_unit

class reactor_serializer(serializers.ModelSerializer):
    class Meta:
        model = reactor_unit
        fields = ["id", "PlantName", "DocketNumber", "LicenseNumber","ReactorType","Location","Owner","NRC_Region"]

