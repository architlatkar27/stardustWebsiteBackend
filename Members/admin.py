from django.contrib import admin
from .models import Student, Technical, Rocketry, NonTechnical, Faculty
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'usn', 'branch', 'year', 'email')
    # search_fields = ['name', 'branch', 'year', 'usn']
    list_display = ('name', 'is_active')
    search_fields = ('name',)

class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('subsystem', 'position', 'member')
    search_fields = ['subsystem', 'position', 'member__name']

class RocketryAdmin(admin.ModelAdmin):
    list_display = ('subsystem', 'position', 'member')
    search_fields = ['subsystem', 'position', 'member__name']

class NonTechAdmin(admin.ModelAdmin):
    list_display = ('team','position', 'member')
    search_fields = ['team','position', 'member__name']

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept', 'position')
    search_fields = ['name', 'dept', 'position']

admin.site.register(Student, StudentAdmin)
admin.site.register(Technical, TechnicalAdmin)
admin.site.register(Rocketry, RocketryAdmin)
admin.site.register(NonTechnical, NonTechAdmin)
admin.site.register(Faculty, FacultyAdmin)
