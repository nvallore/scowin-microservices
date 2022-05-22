from django.db import models

# Create your models here.
class Student(models.Model):
    """
    Student model added here
    """
    id = models.IntegerField(primary_key=True, max_length=4)
    studentName = models.CharField(max_length=32)
    dob = models.DateTimeField()
    #dob = models.DateField()
    gender = models.CharField(max_length=32)
    grade = models.CharField(max_length=2)
    section = models.CharField(max_length=1)
    aadharID = models.CharField(max_length=12)
    existingComorbidites = models.CharField(max_length=300, null=True, blank=True)
    bloodGroup = models.CharField(max_length=3)
    vaccination = models.IntegerField(null=True)

