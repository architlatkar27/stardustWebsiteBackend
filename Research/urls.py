from django.urls import path
from Research.views import research_view

app_name = 'Research'

urlpatterns = [
    path('', research_view, name="research"),
    
]