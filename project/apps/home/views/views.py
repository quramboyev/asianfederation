from django.shortcuts import render
from apps.home.models import DocumentModel


def home(request):
    return render(request, 'home.html')


def events_calendar(request):
    document = DocumentModel.objects.all()[:1][0]
    return render(request, 'events-calendar.html', context={'document': document})


def about_us(request):
    return render(request, 'about-us.html')

def antidoping(request):
    return render(request, 'antidoping.html')

def command(request):
    return render(request, 'command.html')
