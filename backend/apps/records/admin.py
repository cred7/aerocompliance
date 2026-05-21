from django.contrib import admin

# Register your models here.
from apps.records.models.document import Document
from apps.records.models.document_link import DocumentLink

admin.site.register(Document)
admin.site.register(DocumentLink)
