from datetime import datetime
from django.shortcuts import render
from apps.home.models import DocumentModel, DocTypeChoice, ImageModel, AboutUsModel, CalendarModel, GalleryModel, \
    GoalModel


def home(request):
    now = datetime.now()
    rule = DocumentModel.objects.filter(type=DocTypeChoice.RULE).translated().first()
    images = ImageModel.objects.filter(for_date__lte=now)
    about = GalleryModel.objects.filter(selected=True).translated().first()
    events = CalendarModel.objects.filter(_from__gte=now).translated()

    return render(request, 'home.html',
        context={
            'rule': rule,
            'images': images,
            'about': about,
            'events': events,
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
    about = AboutUsModel.objects.filter(selected=True).translated().first()
    goals = GoalModel.objects.filter(disabled=False).translated()
    return render(request, 'about-us.html', context={'about': about, 'goals': goals})


def antidoping(request):
    return render(request, 'antidoping.html')


def command(request):
    return render(request, 'command.html')


def history(request):
    return render(request, 'history.html')
