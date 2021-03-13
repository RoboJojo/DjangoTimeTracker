from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from timeTracking.models import Project, timeSpent
import timeTracker.forms as forms
from django.utils import timezone

def timeTracking(request):
    
    allProjects = Project.objects.all()

    context = {
        'allProjects': allProjects,
    }

    return render(request, 'timeTracking.html', context)

def startTime(request):
   if request.method == "POST":
       project = Project.objects.get(ID = request.POST['projectID'])
       now = timezone.now()
       startTimeSpent = timeSpent(project = project, startTime = now)
       startTimeSpent.save()
       return JsonResponse({ "success" : True })
   return JsonResponse({ "success" : False })

def stopTime(request):
    if request.method == "POST":
        if timeSpent.objects.filter().first():
        # need to have a check if there are more than one entries without an end time. should only be one
        # also need some way to make sure the POST request isn't coming from anywhere except the timeTracking page
            endTimeSpent = timeSpent.objects.order_by("startTime").last()
            now = timezone.now()            
            endTimeSpent.endTime = now
            endTimeSpent.duration = endTimeSpent.endTime - endTimeSpent.startTime
            project = endTimeSpent.project
            project.timeSpent += endTimeSpent.duration
            endTimeSpent.save()
            project.save()
            return JsonResponse({ "success":True })
    return JsonResponse({ "success":False })
            
def clearDurations(request):
          timeSpent.objects.all().delete()
          Project.objects.all().delete()
          return JsonResponse({ "success":True })
        
def registerProject(request):
    
    if request.method == "POST":
        form = forms.newProject(request.POST) 
        if form.is_valid(): 
            newProject = form.save()             
            messages.success(request, 'New Project successfuly created')
    form = forms.newProject()
        
    return render(request, "addProject.html", { 'form' : form }) 
       
def projects(request):
    allProjects = Project.objects.all()
    chartData = {'labels': [], 'data': []}
    for project in allProjects:
        chartData['labels'].append(project.name)
        chartData['data'].append(project.timeSpent.total_seconds())
    context = { 'allProjects' : allProjects, 'chartData' : chartData}
    
    return render(request , 'projects.html' , context)

def durations(request):
    allDurations = timeSpent.objects.all()

    context = {'allDurations' : allDurations}

    return render(request , 'timeDurations.html' , context)
