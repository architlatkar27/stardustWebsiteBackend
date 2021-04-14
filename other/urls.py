from django.urls import path
from .views import home_view, ss_view, contact_view

app_name = 'other'

urlpatterns = [
    path('', home_view, name="home"), 
    path('subsystems', ss_view, name="subsystems"),
    path('contact', contact_view, name="contact")
]