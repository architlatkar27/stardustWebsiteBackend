from django.urls import path
from .views import acheivements_view

app_name = "Achievements"

urlpatterns = [
    path('', acheivements_view, name="achievements"), 
]