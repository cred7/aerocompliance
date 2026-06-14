from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.mel.models.mel_item import MELItem
from apps.mel.api.serializers.mel_serializer import MELSerializer
from apps.mel.services.mel_service import MELService
from rest_framework.permissions import IsAuthenticated
from apps.audits.services.audit_service import AuditService


class MELViewSet(viewsets.ModelViewSet):
    queryset = MELItem.objects.select_related("aircraft").order_by("-reported_date")
    serializer_class = MELSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter by aircraft if provided"""
        queryset = super().get_queryset()
        aircraft_id = self.request.query_params.get("aircraft_id")
        status = self.request.query_params.get("status")
        category = self.request.query_params.get("category")

        if aircraft_id:
            queryset = queryset.filter(aircraft_id=aircraft_id)
        if status:
            queryset = queryset.filter(status=status)
        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def perform_create(self, serializer):
        mel = MELService.create_mel(
            data=serializer.validated_data, user=self.request.user
        )

        # Audit the creation
        try:
            AuditService.log_create(
                user=self.request.user,
                instance=mel,
                after=self.get_serializer(mel).data,
            )
        except Exception:
            # Don't break creation if audit logging fails; log silently
            pass

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Capture before state for audit logging
        instance = self.get_object()
        before_data = self.get_serializer(instance).data

        response = super().update(request, *args, **kwargs)

        try:
            AuditService.log_update(
                user=request.user,
                instance=instance,
                before_data=before_data,
                after=response.data,
            )
        except Exception:
            # Don't break the update flow if auditing fails
            pass

        return response

    @action(detail=False, methods=["get"])
    def by_aircraft(self, request):
        """Get MEL items for a specific aircraft"""
        aircraft_id = request.query_params.get("aircraft_id")
        if not aircraft_id:
            return Response({"error": "aircraft_id parameter required"}, status=400)

        mel_items = self.get_queryset().filter(aircraft_id=aircraft_id)
        serializer = self.get_serializer(mel_items, many=True)
        return Response(serializer.data)
