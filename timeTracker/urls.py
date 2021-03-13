"""timeTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import RedirectView
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from timeTracker.views import index
from timeTracking.views import timeTracking, registerProject, projects, startTime, stopTime, durations, clearDurations
urlpatterns = [
    path('',                RedirectView.as_view(url='index/', permanent=True)),
    path('index/',          index,          name='index'),
    path('timeTracking/',   timeTracking,   name="timeTracking"),
    path('registerProject/', registerProject, name='registerProject'),
    path('projects/',       projects,       name='projects'),
    path('startTime/',      startTime,      name='startTime'),
    path('stopTime/',       stopTime,       name='stopTime'),
    path('durations/',      durations,      name='durations'),
    path('clearDurations/', clearDurations, name='clearDurations'), #bad, will delete all your stuff!!!
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # static file servong during developement
