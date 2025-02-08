from datetime import datetime
from django.shortcuts import render
from apps.home.models import DocumentModel, DocTypeChoice, ImageModel, AboutUsModel, CalendarModel

def home(request):
    now = datetime.now()
    rule = DocumentModel.objects.filter(type=DocTypeChoice.RULE).translated().first()
    images = ImageModel.objects.filter(for_date__lte=now)
    about = AboutUsModel.objects.filter(selected=True).translated().first()
    events_old = CalendarModel.objects.filter(_from__lt=now).translated()
    events = CalendarModel.objects.filter(_from__gte=now).translated()

    return render(request, 'home.html',
        context={
            'rule': rule,
            'images': images,
            'about': about,
            'events': events,
            'events_old': events_old,
        }
    )

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
