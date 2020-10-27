from django import forms 
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    #for placeholder
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model=Task #which model we have to use for forms
        fields='__all__' #what field we want in our form
        