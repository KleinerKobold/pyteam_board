from django.db import models

# Create your models here.
class Skill (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(blank=True, null=True)
    beginner = models.CharField(blank=True, null=True)
    intermediate = models.CharField(blank=True, null=True)
    expert = models.CharField(blank=True, null=True)

    def __str__(self) -> str:
        return name
