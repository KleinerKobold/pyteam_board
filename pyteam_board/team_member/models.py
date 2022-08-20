from tkinter import CASCADE
from django.db import models
from skills.models import Skill

# Create your models here.
class Person(models.Model):
    name_text = models.CharField(max_length=200)
    entered_date = models.DateField('date entered')
    exited_date = models.DateField('date exited', blank=True, null=True)

    def __str__(self):
        return f"{self.name_text}"

class Experience(models.Model):
    name_text = models.CharField(max_length=200)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, default=1)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)    
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"Experience {self.name_text} of {self.person} with {self.level}"

class Observation(models.Model):
    name = models.CharField(max_length=200)
    describtion = models.CharField(max_length=2000, blank=True)
    date = models.DateTimeField('observed on',auto_now_add=True, blank=True)
    persons = models.ManyToManyField(Person, through="Observed")

    def __str__(self) -> str:
        return self.name
    
class Observed(models.Model):
    """https://stackoverflow.com/questions/9449882/django-and-models-with-multiple-foreign-keys"""
    person= models.ForeignKey(Person, on_delete=models.CASCADE)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Relation ({self.person} - {self.observation})"


