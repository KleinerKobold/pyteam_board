from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Observation, Observed, Person, Experience

admin.site.register(Person)
admin.site.register(Experience)
admin.site.register(Observation)
admin.site.register(Observed)