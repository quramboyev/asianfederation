from django.db import models


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
