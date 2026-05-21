from apps.records.models.document import Document


def get_aircraft_documents(aircraft_id: int):
    return Document.objects.filter(
        aircraft_id=aircraft_id
    ).order_by("-uploaded_at")


def get_documents_by_type(doc_type: str):
    return Document.objects.filter(type=doc_type)
