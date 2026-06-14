from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.records.models.document import Document
from apps.records.api.serializers.document_serializer import DocumentSerializer
from apps.records.services.document_service import DocumentService
from rest_framework.permissions import IsAuthenticated


class DocumentViewSet(viewsets.ModelViewSet):

    queryset = Document.objects.select_related("aircraft", "uploaded_by").order_by(
        "-uploaded_at"
    )
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter by aircraft and type if provided"""
        queryset = super().get_queryset()
        aircraft_id = self.request.query_params.get("aircraft_id")
        doc_type = self.request.query_params.get("type")

        if aircraft_id:
            queryset = queryset.filter(aircraft_id=aircraft_id)
        if doc_type:
            queryset = queryset.filter(type=doc_type)

        return queryset

    def perform_create(self, serializer):
        DocumentService.upload_document(
            data=serializer.validated_data, user=self.request.user
        )

    @action(detail=False, methods=["get"])
    def by_aircraft(self, request):
        """Get documents for a specific aircraft"""
        aircraft_id = request.query_params.get("aircraft_id")
        if not aircraft_id:
            return Response({"error": "aircraft_id parameter required"}, status=400)

        documents = self.get_queryset().filter(aircraft_id=aircraft_id)
        serializer = self.get_serializer(documents, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def by_type(self, request):
        """Get documents filtered by type"""
        doc_type = request.query_params.get("type")
        if not doc_type:
            return Response({"error": "type parameter required"}, status=400)

        documents = self.get_queryset().filter(type=doc_type)
        serializer = self.get_serializer(documents, many=True)
        return Response(serializer.data)
