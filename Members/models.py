from django.db import models
import re
# Create your models here.
class Student(models.Model):

    COREPOSTS = (
        ("None", "None"),
        ("SPM", "Project Manager"),
        ("PM", "Project Director"),
        #("PS", "Project Supervisor"),
        ("MM", "Mission Manager"),
        ("MD", "Mission Director"),
        ("TM", "Team Manager")
        #("MS", "Mission Supervisor"),
        #("OH", "Operation Head"),
    )  
    
    objects        = models.Manager()

    sdid           = models.CharField(max_length=8, primary_key=True, default="sd00de01")
    usn            = models.CharField(max_length=10, unique=True, blank=False)
    name           = models.CharField(max_length=60, blank=False)
    branch         = models.CharField(max_length=40)
    #year           = models.IntegerField()
    email          = models.EmailField()
    phone          = models.IntegerField()
    image          = models.ImageField(null=True, blank=True, upload_to='student_photo/')
    is_active      = models.BooleanField(default=True)
    is_core        = models.BooleanField(default=False)
    core_position  = models.CharField(choices=COREPOSTS, max_length=4, null=True)

    def __str__(self):
        return self.name


class Technical(models.Model):
    
    SUBSYSTEMS = (
        #("None", "None"),
        ("PL", "Payload"),
        ("ADCS", "ADCS"),
        ("EPS", "Power"),
        ("ODHS", "ODHS"),
        ("GC", "Communication"),
        ("STR", "Structure"),
    )
    SSPOSTS = (
        #("None", "None"),
        ("SSH", "Subsystem Head"),
        ("CSE", "Chief System Engineer"),
        ("SE", "System Engineer"),
        ("SSE", "Subsystem Engineer")
    )

    objects        = models.Manager()

    member         = models.ForeignKey(Student, on_delete=models.CASCADE)
    subsystem      = models.CharField(choices=SUBSYSTEMS, max_length=5)
    position       = models.CharField(choices=SSPOSTS, max_length=5)



class NonTechnical(models.Model):
    
    NONTECH = (
        ("WEB","Website"),
        ("SPR","Public Relations and Sponsorship"),
        #("SP","Sponsorship"),
        ("SM","Social Media"),
        ("DOC","Documentation"),
        ("FIN","Finance")
    )

    objects        = models.Manager()

    member         = models.ForeignKey(Student, on_delete=models.CASCADE)
    team           = models.CharField(choices=NONTECH, max_length=4)

