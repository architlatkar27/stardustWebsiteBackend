from django.urls import path
from .views import team_view

app_name = "Members"

urlpatterns = [
    path('', team_view, name="team"),
]