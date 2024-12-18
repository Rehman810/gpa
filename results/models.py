from django.db import models

class Result(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    linear_algebra = models.CharField(max_length=2)
    oop_theory = models.CharField(max_length=2)
    oop_practical = models.CharField(max_length=2)
    pakistan_studies = models.CharField(max_length=2)
    islamic_studies = models.CharField(max_length=2)
    digital_logic_theory = models.CharField(max_length=2)
    digital_logic_practical = models.CharField(max_length=2)
    communication_skills = models.CharField(max_length=2)

    def __str__(self):
        return self.roll_no
