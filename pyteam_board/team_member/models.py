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
    person = models.ForeignKey(Person, on_delete=models.CASCADE)    
    level = models.IntegerField(default=0)

    def __str__(self):
        return f"Experience {self.name_text} of {self.person} with {self.level}"

