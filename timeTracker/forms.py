from django import forms
from timeTracking.models import Project, User, timeSpent

class newProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class newUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        
# class startTime(forms.ModelForm):
#     class Meta:
#         model = timeSpent
#         fields = "__all__"