from rest_framework import serializers
from apps.compliance.models.compliance_snapshot import ComplianceSnapshot


class ComplianceSnapshotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComplianceSnapshot
        fields = "__all__"
