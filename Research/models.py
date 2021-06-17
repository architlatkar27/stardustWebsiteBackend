from django.db import models
from Members.models import Student

# Create your models here.
class ResearchPaper(models.Model):

    objects        = models.Manager()

    
    title          = models.CharField(max_length=250, null=False, blank=False)
    year           = models.IntegerField(null=False, blank=False)
    author         = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="author")
    conference     = models.CharField(max_length=200, null=False, blank=False)
    #abstract       = models.TextField(max_length=1000, null=False, blank=False)
    abstract_pdf      = models.URLField(null=False, blank=False)  