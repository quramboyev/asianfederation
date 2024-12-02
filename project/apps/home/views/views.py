from django.shortcuts import render
from apps.home.models import DocumentModel


def home(request):
    return render(request, 'home.html')


def events_calendar(request):
    document = DocumentModel.objects.all()
    if document.exists():
        document = document[0]
    else: 
        document = None
    return render(request, 'events-calendar.html', context={'document': document})


def about_us(request):
    return render(request, 'about-us.html')


def antidoping(request):
    return render(request, 'antidoping.html')


def command(request):
    return render(request, 'command.html')


def history(request):
    return render(request, 'history.html')
