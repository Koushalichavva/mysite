from django.db import models

# Create your models here.
class department(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField()

class Student(models.Model):

    # Choices for dropdowns
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    DEPT_CHOICES = [
        ('cse','CSE'),
        ('ece','ECE'),
        ('mech','MECH'),
        ('it','IT'),
    ]

    YEAR_CHOICES = [
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
    ]

    MODE_CHOICES = [
        ('online','Online'),
        ('offline','Offline'),
    ]

    TECH_CHOICES = [
        ('python','Python'),
        ('java','Java'),
        ('c++','C++'),
        ('webdev','Web Development'),
    ]

    STATE_CHOICES = [
        ('AndhraPradesh','Andhra Pradesh'),
        ('Telangana','Telangana'),
        ('Karnataka','Karnataka'),
        ('Tamilnadu','Tamil Nadu'),
    ]

    # Personal Details
    name = models.CharField(max_length=100)
    email = models.EmailField()
    p_number = models.CharField(max_length=10)
    dob = models.DateField()  # Forms will automatically render a date input / calendar

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # Academic Details
    department = models.CharField(max_length=50, choices=DEPT_CHOICES)
    yostudy = models.CharField(max_length=10, choices=YEAR_CHOICES)
    rollnumber = models.CharField(max_length=20)

    # Address Details
    address = models.TextField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    pincode = models.CharField(max_length=6)

    # Skills and Preferences
    technical_Skills = models.CharField(max_length=50, choices=TECH_CHOICES)
    preferred_mode = models.CharField(max_length=20, choices=MODE_CHOICES)

    # Additional Information
    resume_upload = models.FileField(upload_to='resumes/')
    about_yourself = models.TextField()
    aggree = models.BooleanField()



    def __str__(self):
        return self.name
