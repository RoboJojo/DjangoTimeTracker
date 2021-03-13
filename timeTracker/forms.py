from django import forms
from timeTracking.models import Project

class newProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"