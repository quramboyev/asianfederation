from django.db import models


class DocumentModel(models.Model):
    name = models.CharField(max_length=64)
    file = models.FileField(upload_to='documents/')

    def __str__(self) -> str:
        return f"{self.name} - {self.file.name}"
    
    class Meta:
        db_table = "documents"
        verbose_name = "Document"
        verbose_name_plural = "Documents"
