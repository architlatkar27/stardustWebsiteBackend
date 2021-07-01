from django.db import models
from cloudinary.models import CloudinaryField
import re
# Create your models here.
class Student(models.Model):

    COREPOSTS = (
        ("None", "None"),
        ("SPM", "Senior Project Manager"),
        ("PM", "Project Manager"),
        #("PS", "Project Supervisor"),
        ("MM", "Mission Manager"),
        ("MD", "Mission Director"),
        ("TM", "Team Manager"),
        ("RH", "Rocketry Head"),
        ("NH","Non-Technical Head"),
        #("MS", "Mission Supervisor"),
        #("OH", "Operation Head"),
    ) 

    STATUS = (
        ('F', "Founder"),
        ('C', "Core Member"),
    ) 
    DEPT = (
        ("CSE", "Computer Science and Engineering"),
        ("ECE", "Electronics and Communication Engineering"),
        ("ETE", "Electronics and Telecommunication Engineering"),
        ("ISE", "Information Science and Engineering"),
        ("EIE", "Electronics and Instrumentation Engineering"),
        ("EEE", "Electronics and Electrical Engineering"),
        ("ML", "Medical Electronics"),
        ("BT", "BioTechnology"),
        ("MECH", "Mechanical Engineering"),
        ("CV", "Civil Engineering"),
        ("CHE", "Chemical Engineering"),
        ("IEM", "Industrial Engineering and Managment")
    )
    
    objects        = models.Manager()

    # sdid         = models.CharField(max_length=8, primary_key=True, default="sd00de01")
    # usn          = models.CharField(max_length=10, unique=True, blank=False)
    name           = models.CharField(max_length=60, blank=False, primary_key=True)
    branch         = models.CharField(max_length=40, choices = DEPT)
    # year         = models.IntegerField()
    email          = models.EmailField(null= True,blank=True)
    linkedin       = models.URLField(null= True,blank=True)
    # phone        = models.IntegerField()
    #image         = models.ImageField(null=True, blank=True, upload_to='student_photo/')
    image          = CloudinaryField('image',null=True, blank=True)
    status         = models.CharField(null=True, blank=True, max_length=10, choices=STATUS)
    is_active      = models.BooleanField(default=True)
    core_position  = models.CharField(choices=COREPOSTS, default='None',max_length=4, null=True, blank=True)
    rank           = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if self.status == 'C' and self.core_position == "None":
            raise ValueError("Core member must have a core position")
        elif self.status != 'C' and self.core_position != "None":
            raise ValueError("Non core member cannot be given a core position")
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Technical(models.Model):
    
    SUBSYSTEMS = (
        #("None", "None"),
        ("PL", "Payload Subsystem"),
        ("ADCS", "Attitude Determination and Control Subsystem"),
        ("EPS", "Electrical Power System Subsystem"),
        ("ODHS", "On Board Data Handling Susbsytem"),
        ("GC", "Ground Control and Communication Subsystem"),
        ("STR", "Structures and Thermal Susbsystem")
    )
    SSPOSTS = (
        ("None", "None"),
        ("SSH", "Subsystem Head"),
        ("CSE", "Chief System Engineer"),
        ("SE", "System Engineer"),
        ("SSE", "Subsystem Engineer")
    )

    objects        = models.Manager()

    member         = models.OneToOneField(Student, on_delete=models.CASCADE, unique=True)
    subsystem      = models.CharField(choices=SUBSYSTEMS, max_length=5)
    position       = models.CharField(choices=SSPOSTS, max_length=5)
    rank           = models.IntegerField(default=1,blank=False)

    def __str__(self):
        return self.member.name #+ self.subsystem
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class Rocketry(models.Model):
    
    SUBSYSTEMS = (
        #("None", "None"),
        ("AS", "Aerodynamics and Structures"),
        ("GCS", "Guidance and Control System"),
        ("PS", "Propulsion System")
    )
    RPOSTS = (
        ("None", "None"),
        ("SSH", "Subsystem Head"),
        ("CSE", "Chief System Engineer"),
        ("SE", "System Engineer"),
        ("SSE", "Subsystem Engineer")
    )

    objects        = models.Manager()

    member         = models.OneToOneField(Student, on_delete=models.CASCADE, unique=True)
    subsystem      = models.CharField(choices=SUBSYSTEMS, max_length=5)
    position       = models.CharField(choices=RPOSTS, max_length=5)
    rank           = models.IntegerField(default=1,blank=False)

    def __str__(self):
        return self.member.name #+ self.subsystem
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class NonTechnical(models.Model):
    
    NONTECH = (
        ("WEB","Website and Design"),
        ("SPR","Public Relations and Sponsorship"),
        #("SP","Sponsorship"),
        ("SM","Social Media"),
        ("DOC","Documentation"),
    )

    NPOST = (
        ("None", "None"),
        ("H", "Head"),
        ("SH","Sub Head"),
        ("M","Member")
    )

    objects        = models.Manager()

    member         = models.OneToOneField(Student, on_delete=models.CASCADE, unique=True)
    team           = models.CharField(choices=NONTECH, max_length=4)
    position       = models.CharField(choices=NPOST,default='None', max_length=5)
    rank           = models.IntegerField(default=1,blank=False)

    def __str__(self):
        return self.member.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Faculty(models.Model):
    objects       = models.Manager()

    DEPT = (
        ("CSE", "Computer Science and Engineering"),
        ("ECE", "Electronics and Communication Engineering"),
        ("ETE", "Electronics and Telecommunication Engineering"),
        ("ISE", "Information Science and Engineering"),
        ("EIE", "Electronics and Instrumentation Engineering"),
        ("EEE", "Electronics and Electrical Engineering"),
        ("ML", "Medical Electronics"),
        ("BT", "BioTechnology"),
        ("MECH", "Mechanical Engineering"),
        ("CV", "Civil Engineering"),
        ("CHE", "Chemical Engineering"),
        ("IEM", "Industrial Engineering and Managment")
    )

    POST = (
        ("HOD", "Head of Department"),
        ("ASCP", "Associate Professor"),
        ("ASSP", "Assistant Professor"),
        ("VF", "Visiting Faculty"),
    )
    
    #image         = models.ImageField(null=True, blank=True, upload_to = 'faculty_photo/')
    image          = CloudinaryField('image',null=True, blank=True)
    name          = models.CharField(null=False, blank=False, primary_key=True, max_length=60)
    position      = models.CharField(null=False, blank=False, choices=POST, max_length=40)
    dept          = models.CharField(null=False, blank=False, choices=DEPT, max_length=40)
    rank          = models.IntegerField(null=True)