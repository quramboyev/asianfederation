from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class DocTypeChoice(models.TextChoices):
    CALENDAR = 'C', _('Calendar')
    ANTI_DOPING = 'A', _('Anti Doping')
    RULE = 'R', _('Rule')


class DocumentModel(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=64),
        file = models.FileField(upload_to='documents/')
    )
    type = models.CharField(choices=DocTypeChoice.choices)

    def __str__(self) -> str:
        return f"{self.name} - {self.file.name}"
    
    class Meta:
        db_table = "documents"
        verbose_name = "Document"
        verbose_name_plural = "Documents"


class CalendarModel(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=256),
        organizer = models.CharField(max_length=256),
        location = models.CharField(max_length=256)
    )
    _from = models.DateField()
    to = models.DateField()

    class Meta:
        db_table = "calendars"
        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"

    def __str__(self) -> str:
        return f"{self.name} - {self.organizer}"
