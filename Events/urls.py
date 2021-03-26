from django.urls import path
from Events.views import events_view

app_name = "Events"

urlpatterns = [
    path('', events_view, name="events"),

]
