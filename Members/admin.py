from django.contrib import admin
from .models import Student, Technical, NonTechnical
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'usn', 'branch', 'year', 'email')
    search_fields = ['name', 'branch', 'year', 'usn']

class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('subsystem', 'position', 'member')
    search_fields = ['subsystem', 'position', 'member']

class NonTechAdmin(admin.ModelAdmin):
    list_display = ('team', 'member')
    search_fields = ['team', 'member']

admin.site.register(Student, StudentAdmin)
admin.site.register(Technical, TechnicalAdmin)
admin.site.register(NonTechnical, NonTechAdmin)
