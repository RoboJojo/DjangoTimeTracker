from django.db import models
from datetime import timedelta
# Create your models here.

class Project(models.Model):
    ID = models.AutoField("Project ID", primary_key = True) # not named id becuase of conflict with python keyword function id()

    name = models.CharField("New Project Name", max_length = 60, unique = True)

    start_date = models.DateTimeField("Start date", auto_now_add = True)

    end_date = models.DateTimeField("End date", null = True, blank = True, auto_now = False, auto_now_add = False)

    timeSpent = models.DurationField("Time spent", blank = True, null = True, default = timedelta(0))

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class timeSpent(models.Model):
    startTime = models.DateTimeField("Start Time")

    endTime = models.DateTimeField("End Time", blank = True, null = True)

    duration = models.DurationField("Timed duration", blank = True, null = True)
    
    project = models.ForeignKey(Project, on_delete = models.CASCADE, unique = False)
    
    class Meta:
        get_latest_by = ['startTime']
