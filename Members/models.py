from django.db import models
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
        ("TM", "Team Manager")
        #("MS", "Mission Supervisor"),
        #("OH", "Operation Head"),
    ) 

    STATUS = (
        ('F', "Founder"),
        ('C', "Core Member"),
        ('TM', "Technical Member"),
        ('NM', 'Nontechnical Member')
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

    # sdid           = models.CharField(max_length=8, primary_key=True, default="sd00de01")
    # usn            = models.CharField(max_length=10, unique=True, blank=False)
    name           = models.CharField(max_length=60, blank=False, primary_key=True)
    branch         = models.CharField(max_length=40, choices = DEPT)
    # year           = models.IntegerField()
    email          = models.EmailField()
    linkedin       = models.URLField()
    # phone          = models.IntegerField()
    image          = models.ImageField(null=True, blank=True, upload_to='student_photo/')
    status         = models.CharField(null=True, blank=True, max_length=10, choices=STATUS)
    is_active      = models.BooleanField(default=True)
    core_position  = models.CharField(choices=COREPOSTS, max_length=4, null=True, blank=True)
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
        ("PL", "Payload"),
        ("ADCS", "ADCS"),
        ("EPS", "Power"),
        ("ODHS", "ODHS"),
        ("GC", "Communication"),
        ("STR", "Structure and Thermal"),
    )
    SSPOSTS = (
        #("None", "None"),
        ("SSH", "Subsystem Head"),
        ("CSE", "Chief System Engineer"),
        ("SE", "System Engineer"),
        ("SSE", "Subsystem Engineer")
    )

    objects        = models.Manager()

    member         = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True)
    subsystem      = models.CharField(choices=SUBSYSTEMS, max_length=5)
    position       = models.CharField(choices=SSPOSTS, max_length=5)

    def __str__(self):
        pass
    
    def save(self, *args, **kwargs):
        pass



class NonTechnical(models.Model):
    
    NONTECH = (
        ("WEB","Website"),
        ("SPR","Public Relations and Sponsorship"),
        #("SP","Sponsorship"),
        ("SM","Social Media"),
        ("DOC","Documentation"),
        ("FIN","Finance")
    )

    NPOST = (
        #("None", "None"),
        ("H", "Head"),
        ("SH","Sub Head"),
        ("M","Member")
    )

    objects        = models.Manager()

    member         = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True)
    team           = models.CharField(choices=NONTECH, max_length=4)
    position       = models.CharField(choices=NPOST,default='M', max_length=5)

    def __str__(self):
        pass

    def save(self, *args, **kwargs):
        pass


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
    
    image         = models.ImageField(null=True, blank=True, upload_to = 'faculty_photo/')
    name          = models.CharField(null=False, blank=False, primary_key=True, max_length=60)
    position      = models.CharField(null=False, blank=False, choices=POST, max_length=40)
    dept          = models.CharField(null=False, blank=False, choices=DEPT, max_length=40)
    rank          = models.IntegerField(null=True)