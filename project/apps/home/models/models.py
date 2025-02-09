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


class PositionChoice(models.TextChoices):
    MANAGEMENT = "M", _('Management')
    COMMITTEE = "C", _('Committee')
    PRESIDIUM = "P", _('Presidium')


class CommandModel(TranslatableModel):
    image = models.ImageField(null=True, blank=True, upload_to='documents/')
    translations = TranslatedFields(
        first_name=models.CharField(max_length=15, verbose_name=_("First name")),
        last_name=models.CharField(max_length=20, verbose_name=_("Last name")),
        responsibility=models.CharField(max_length=32, verbose_name=_("Responsibility")),
        federation=models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Federation")),
    )
    position = models.CharField(max_length=1, choices=PositionChoice.choices, verbose_name=_("Position"), default=PositionChoice.MANAGEMENT)
    class Meta:
        db_table = "command"
        verbose_name = "Member"
        verbose_name_plural = "Members"        

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class EventCalendarModel(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_("Event name")),
        date=models.CharField(max_length=100, verbose_name=_("Dates of the event")),
        location=models.CharField(max_length=100, verbose_name=_("Location")),
        organizers=models.CharField(max_length=100, verbose_name=_("Conducting organization"))
    )

    class Meta:
        db_table = "eventscalendar"
        verbose_name = _("Events calendar")
        verbose_name_plural = _("Events calendar")

    def __str__(self):
        return f"{self.name}"
