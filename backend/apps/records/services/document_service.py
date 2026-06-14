from apps.records.models.document import Document


class DocumentService:

    @staticmethod
    def upload_document(data, user):

        document = Document.objects.create(uploaded_by=user, **data)

        return document
