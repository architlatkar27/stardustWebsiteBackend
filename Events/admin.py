from django.contrib import admin
from .models import Event
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date' )
    search_fields = ['title', 'start_date']

admin.site.register(Event, EventAdmin)
