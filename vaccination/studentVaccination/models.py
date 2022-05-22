from django.db import models

# Create your models here.
class StudentVaccination(models.Model):
    """
    StudentVaccination model added here
    """
    student = models.PositiveIntegerField()
    vaccinationDate = models.DateTimeField()
    dosage = models.PositiveIntegerField(default=1)
    vaccinationStatus = models.CharField(max_length=32)
    vaccine = models.CharField(max_length=50)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.student)
