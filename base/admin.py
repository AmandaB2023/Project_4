from django.contrib import admin
from .models import Task
# Register your models here.

# Registered model with admin panel.
admin.site.register(Task)