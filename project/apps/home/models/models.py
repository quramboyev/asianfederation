from datetime import datetime

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
    country_code = models.CharField(max_length=3)

    @property
    def from_(self):
        return self._from

    def finished(self):
        return self.to < datetime.now()

    class Meta:
        db_table = "calendars"
        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"

    def __str__(self) -> str:
        return f"{self.name} - {self.organizer}"


class AboutUsModel(TranslatableModel):
    translations = TranslatedFields(
        description=models.TextField(),
    )
    selected = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.selected:
            AboutUsModel.objects.filter(selected=True).update(selected=False)
        super(AboutUsModel, self).save(*args, **kwargs)

    class Meta:
        db_table = "about_us"
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self) -> str:
        return f"{self.description[:10]}:{'selected' if self.selected else ''}"


class GoalModel(TranslatableModel):
    translations = TranslatedFields(
        goal = models.CharField(max_length=256),
    )
    disabled = models.BooleanField(default=False)

    class Meta:
        db_table = "goals"
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __str__(self) -> str:
        return self.goal


