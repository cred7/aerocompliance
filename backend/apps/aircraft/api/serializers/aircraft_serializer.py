from rest_framework import serializers
from apps.aircraft.models.aircraft import Aircraft


class AircraftTypeListSerializer(serializers.Serializer):
    """Simplified aircraft type for nesting"""

    id = serializers.IntegerField()
    manufacturer = serializers.CharField()
    model = serializers.CharField()
    engine_type = serializers.CharField()


class OperatorListSerializer(serializers.Serializer):
    """Simplified operator for nesting"""

    id = serializers.IntegerField()
    name = serializers.CharField()
    code = serializers.CharField()
    country = serializers.CharField()


class MELItemListSerializer(serializers.Serializer):
    """Simplified MEL item for nesting"""

    id = serializers.IntegerField()
    title = serializers.CharField()
    category = serializers.CharField()
    status = serializers.CharField()
    allowed_duration_hours = serializers.FloatField()
    remaining_hours = serializers.FloatField()
    reported_date = serializers.DateTimeField()


class ADComplianceListSerializer(serializers.Serializer):
    """Simplified AD compliance for nesting"""

    id = serializers.IntegerField()
    ad = serializers.SerializerMethodField()
    status = serializers.CharField()
    last_compliance_date = serializers.DateField()
    next_due_date = serializers.DateField()

    def get_ad(self, obj):
        return {
            "id": obj.ad.id,
            "ad_number": obj.ad.ad_number,
            "title": obj.ad.title,
        }


class MaintenanceTaskListSerializer(serializers.Serializer):
    """Simplified maintenance task for nesting"""

    id = serializers.IntegerField()
    title = serializers.CharField()
    interval_type = serializers.CharField()
    interval_value = serializers.FloatField()
    last_performed_date = serializers.DateField()
    is_active = serializers.BooleanField()


class ComplianceSnapshotListSerializer(serializers.Serializer):
    """Simplified compliance snapshot for nesting"""

    id = serializers.IntegerField()
    amp_status = serializers.CharField()
    mel_status = serializers.CharField()
    ad_status = serializers.CharField()
    overall_status = serializers.CharField()
    last_evaluated = serializers.DateTimeField()


class DocumentListSerializer(serializers.Serializer):
    """Simplified document for nesting"""

    id = serializers.IntegerField()
    title = serializers.CharField()
    type = serializers.CharField()
    uploaded_at = serializers.DateTimeField()
    uploaded_by = serializers.SerializerMethodField()

    def get_uploaded_by(self, obj):
        return obj.uploaded_by.username if obj.uploaded_by else None


class AuditLogListSerializer(serializers.Serializer):
    """Simplified audit log for nesting"""

    id = serializers.IntegerField()
    action = serializers.CharField()
    model_name = serializers.CharField()
    timestamp = serializers.DateTimeField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username if obj.user else None


class AircraftSerializer(serializers.ModelSerializer):

    aircraft_type_name = serializers.CharField(
        source="aircraft_type.model",
        read_only=True,
    )

    operator_name = serializers.CharField(
        source="operator.name",
        read_only=True,
    )

    class Meta:
        model = Aircraft
        fields = [
            "id",
            "tail_number",
            "serial_number",
            "manufacture_date",
            "total_flight_hours",
            "total_flight_cycles",
            "status",
            "aircraft_type",
            "aircraft_type_name",
            "operator",
            "operator_name",
            "created_at",
            "updated_at",
        ]


class AircraftDetailSerializer(serializers.ModelSerializer):
    """Comprehensive aircraft detail with all related operational data"""

    aircraft_type = AircraftTypeListSerializer(read_only=True)
    operator = OperatorListSerializer(read_only=True)

    # Operational relationships
    mel_items = serializers.SerializerMethodField()
    ad_compliances = serializers.SerializerMethodField()
    maintenance_tasks = serializers.SerializerMethodField()
    compliance_snapshot = serializers.SerializerMethodField()
    documents = serializers.SerializerMethodField()
    audit_logs = serializers.SerializerMethodField()

    # Summary stats
    total_mel_items = serializers.SerializerMethodField()
    open_mel_items = serializers.SerializerMethodField()
    total_ad_items = serializers.SerializerMethodField()
    overdue_ad_items = serializers.SerializerMethodField()

    class Meta:
        model = Aircraft
        fields = [
            "id",
            "tail_number",
            "serial_number",
            "manufacture_date",
            "total_flight_hours",
            "total_flight_cycles",
            "status",
            "aircraft_type",
            "operator",
            "created_at",
            "updated_at",
            # Related data
            "mel_items",
            "ad_compliances",
            "maintenance_tasks",
            "compliance_snapshot",
            "documents",
            "audit_logs",
            # Summary stats
            "total_mel_items",
            "open_mel_items",
            "total_ad_items",
            "overdue_ad_items",
        ]

    def get_mel_items(self, obj):
        mel_items = obj.mel_items.all()
        return MELItemListSerializer(mel_items, many=True).data

    def get_ad_compliances(self, obj):
        ad_compliances = obj.ad_compliances.all()
        return ADComplianceListSerializer(ad_compliances, many=True).data

    def get_maintenance_tasks(self, obj):
        tasks = obj.maintenance_tasks.all()
        return MaintenanceTaskListSerializer(tasks, many=True).data

    def get_compliance_snapshot(self, obj):
        snapshot = getattr(obj, "compliance_snapshot", None)
        if snapshot:
            return ComplianceSnapshotListSerializer(snapshot).data
        return None

    def get_documents(self, obj):
        documents = obj.documents.all()
        return DocumentListSerializer(documents, many=True).data

    def get_audit_logs(self, obj):
        audit_logs = obj.audit_logs.all().order_by("-timestamp")[:20]  # Last 20
        return AuditLogListSerializer(audit_logs, many=True).data

    def get_total_mel_items(self, obj):
        return obj.mel_items.count()

    def get_open_mel_items(self, obj):
        return obj.mel_items.filter(status__in=["OPEN", "IN_PROGRESS"]).count()

    def get_total_ad_items(self, obj):
        return obj.ad_compliances.count()

    def get_overdue_ad_items(self, obj):
        return obj.ad_compliances.filter(status="OVERDUE").count()
