from django.db import models
from Members.models import Student
# Create your models here.
class Event(models.Model):

    objects        = models.Manager()
    
    title          = models.CharField(max_length=150, null=False,blank=False, unique=True)
    description    = models.TextField(max_length=750, null=False, blank=False)
    start_date     = models.DateField(auto_now=False, auto_now_add=False, verbose_name="start_date")
    end_date       = models.DateField(auto_now=False, auto_now_add=False, verbose_name="end_date")
    start_time     = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="start_time")
    end_time       = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="end_time")
    #details_link   = models.URLField(max_length=250, null=True, blank=True)
    poster         = models.ImageField(null=True, blank=True)
    contact        = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)    