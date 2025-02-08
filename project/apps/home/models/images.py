from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _


class ImageModel(models.Model):
    name = models.CharField(max_length=32)
    file = models.FileField(upload_to='images/')
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    for_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'images'
        verbose_name = 'image'
        verbose_name_plural = 'images'


class GalleryModel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=128, verbose_name=_('title')),
        description = models.TextField(verbose_name=_("Description")),
    )
    selected = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.selected:
            GalleryModel.objects.filter(selected=True).update(selected=False)
        super(GalleryModel, self).save(*args, **kwargs)

    class Meta:
        db_table = 'galleries'
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title
