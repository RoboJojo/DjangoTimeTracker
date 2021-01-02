from django.db import models
from datetime import timedelta
# Create your models here.
class User(models.Model):
    ID = models.AutoField("User ID", primary_key = True) # not named id becuase of conflict with python keyword function id()

    name = models.CharField("User name", max_length = 30)

    projects = models.ManyToManyField("Project", blank = True, verbose_name = "User's projects")

    timeSpent = models.DurationField(blank = True, null = True)
    
    class Meta:
        ordering = ['name']

    def __str__(self): 
        return self.name

class Project(models.Model):
    ID = models.AutoField("Project ID", primary_key = True) # not named id becuase of conflict with python keyword function id()

    name = models.CharField("New Project Name", max_length = 60, unique = True)

    start_date = models.DateTimeField("Start date", auto_now_add = True)

    end_date = models.DateTimeField("End date", null = True, blank = True, auto_now = False, auto_now_add = False)

    timeSpent = models.DurationField("Time spent", blank = True, null = True, default = timedelta(0))

    people = models.ManyToManyField(User, blank = True, verbose_name = "People")

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class timeSpent(models.Model):
    startTime = models.DateTimeField("Start Time")

    endTime = models.DateTimeField("End Time", blank = True, null = True)

    duration = models.DurationField("Timed duration", blank = True, null = True)
    
    #user = models.OneToOneField(User,on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete = models.PROTECT, unique = False)
    
    class Meta:
        get_latest_by = ['startTime']
