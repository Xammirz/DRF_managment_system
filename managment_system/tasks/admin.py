from django.contrib import admin
from django import forms

from managment_system.tasks.models import Task, Team

class TeamAdmin(admin.ModelAdmin):
    formfield_overrides = {
        forms.ModelMultipleChoiceField: {'widget': forms.SelectMultiple},
    }

admin.site.register(Team, TeamAdmin)
admin.site.register(Task)