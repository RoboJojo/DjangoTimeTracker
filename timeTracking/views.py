from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from timeTracking.models import User, Project, timeSpent
import timeTracker.forms as forms
from django.utils import timezone
# Create your views here.
def timeTracking(request):
    
    allProjects = Project.objects.all()
    
    context = {
        'allProjects': allProjects,
       # 'startTime' : forms.startTime()
               }
    
    return render(request,'timeTracking.html', context)

def startTime(request):
   if request.method == "POST":
       project = Project.objects.get(ID=request.POST['projectID'])
       now = timezone.now()
       startTimeSpent = timeSpent(project=project,startTime=now)
       startTimeSpent.save()
       return JsonResponse({"success":True})
   return JsonResponse({"success":False})

def stopTime(request):
    if request.method == "POST":
        if timeSpent.objects.filter().first():
        #need to have a check if there are more than one entries without an end time. should only be one
        #also need some way to make sure the POST request isn't coming from anywhere except the timeTracking page
            endTimeSpent = timeSpent.objects.order_by("startTime").last()
            #project = timeSpentObject.project for later devlopment for updating Projects table
            now = timezone.now()            
            endTimeSpent.endTime = now
            endTimeSpent.duration = endTimeSpent.endTime - endTimeSpent.startTime
            
            project = endTimeSpent.project
            project.timeSpent += endTimeSpent.duration
            
            endTimeSpent.save()
            project.save()
            return JsonResponse({"success":True})
    return JsonResponse({"success":False})
            
def clearDurations(request):
          timeSpent.objects.all().delete()
          Project.objects.all().delete()
          User.objects.all().delete()
          return JsonResponse({"success":True})
        
def registerProject(request):
    
    if request.method == "POST":
        form = forms.newProject(request.POST) 
        if form.is_valid(): 
            newProject = form.save() 
            for user in form.cleaned_data['people']:
                user.projects.add(newProject)     
            
            messages.success(request, 'New Project successfuly created')
    form = forms.newProject()
        
    return render(request,"addProject.html",{'form': form}) 
       
def projects(request):
    allProjects = Project.objects.all()
        
    context = {'allProjects': allProjects}
    
    return render(request , 'projects.html' , context)

def registerUser(request):
    
    if request.method == "POST":
        form = forms.newUser(request.POST) 
        if form.is_valid(): 
            newUser = form.save()
            for project in form.cleaned_data["projects"]:
                project.people.add(newUser)
    else:
         form = forms.newUser()
    
    return render(request,"addUser.html",{'form': form}) 

def users(request):
    allUsers = User.objects.all()
        
    context = {'allUsers': allUsers}
    
    return render(request , 'users.html' , context)

def durations(request):
    allDurations = timeSpent.objects.all()
        
    context = {'allDurations': allDurations}
    
    return render(request , 'timeDurations.html' , context)
