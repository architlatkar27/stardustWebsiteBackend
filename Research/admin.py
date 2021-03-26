from django.contrib import admin
from Research.models import ResearchPaper
# Register your models here.
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'conference', 'year')
    search_fields = ['title', 'author', 'conference', 'year']


admin.site.register(ResearchPaper, ResearchAdmin)