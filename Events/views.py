from django.shortcuts import render
from .models import Event
from datetime import date
# Create your views here.
def events_view(request):
    context = {}
    all_events = Event.objects.all()
    today = date.today()
    context["upcoming"] = filter(lambda x: x.start_date>=today, all_events)
    context["ongoing"] = filter(lambda x: x.start_date<today and x.end_date>today, all_events)
    context["past"] = filter(lambda x: x.start_date<today and x.end_date<today, all_events)
    return render(request,'Events/events.html',context)