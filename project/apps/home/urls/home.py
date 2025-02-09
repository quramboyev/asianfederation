from django.urls import path
from ..views.views import home, events_calendar, about_us, anti_doping, command, history

urlpatterns = [
    path('', home, name='home'),
    path('calendar/', events_calendar, name='events_calendar'),
    path('about_us/', about_us, name='about_us'),
    path('antidoping/', anti_doping, name='antidoping'),
    path('command/', command, name='command'),
    path('history/', history, name='history')
]