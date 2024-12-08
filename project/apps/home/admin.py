from django.contrib import admin
from .models import DocumentModel, ImageModel
from parler.admin import TranslatableAdmin


admin.site.register(DocumentModel, TranslatableAdmin)
admin.site.register(ImageModel, TranslatableAdmin)
