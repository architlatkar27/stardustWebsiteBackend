from django.db import models
from Members.models import Student
from cloudinary.models import CloudinaryField

# Create your models here.
class Achievement(models.Model):
    objects        = models.Manager()
    title          = models.CharField(max_length=150, null=False, blank=False, unique=True)
    description    = models.TextField(max_length=750, null=False, blank=False)
    date           = models.DateField(auto_now=False, auto_now_add=False, verbose_name="prize_date")
    #photo         = models.ImageField(null=True, blank=True)
    photo          = CloudinaryField('image',null=True, blank=True)
    
    def __str__(self):
        return self.title