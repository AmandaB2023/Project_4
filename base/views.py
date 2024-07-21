from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
# Create your views here.
# Inherits from  thus has all the functionality ListView has.
class TaskList(ListView):
    model = Task