from ..models import ImageModel
from django.shortcuts import render


def gallery(request):
    images = ImageModel.objects.all()
    return render(request, 'gallery.html', {'images': images})
