from django.contrib import admin
from .models import Achievement
# Register your models here.

class AchievementManager(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ['title', 'date']

admin.site.register(Achievement, AchievementManager)
