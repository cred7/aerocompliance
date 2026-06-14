from rest_framework import serializers
from apps.ad.models.ad_compliance import ADCompliance


class ADComplianceSerializer(serializers.ModelSerializer):

    ad_number = serializers.CharField(source="ad.ad_number", read_only=True)
    ad_title = serializers.CharField(source="ad.title", read_only=True)
    aircraft_tail = serializers.CharField(source="aircraft.tail_number", read_only=True)

    class Meta:
        model = ADCompliance
        fields = [
            "id",
            "aircraft",
            "aircraft_tail",
            "ad",
            "ad_number",
            "ad_title",
            "status",
            "last_compliance_fh",
            "last_compliance_fc",
            "last_compliance_date",
            "next_due_date",
            "created_at",
            "updated_at",
        ]
