from django.db import models

# Create your models here.
class Skill (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024,blank=True, null=True)
    beginner = models.CharField(max_length=1024,blank=True, null=True)
    intermediate = models.CharField(max_length=1024,blank=True, null=True)
    expert = models.CharField(max_length=1024,blank=True, null=True)
    parent = models.ForeignKey("self",on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
