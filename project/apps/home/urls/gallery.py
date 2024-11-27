from django.urls import path
from apps.home.views.gallery import gallery

urlpatterns = [
    path('gallery/', gallery, name='gallery'),
]