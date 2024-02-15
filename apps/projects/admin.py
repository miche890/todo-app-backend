from django.contrib import admin
from .models import State, Project, Task
from .forms import ProjectForm

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
  form = ProjectForm
  list_display = ['name', 'user']
  list_filter = ['user']
  search_fields = ['name']
      
admin.site.register(Project, ProjectAdmin)

class StateAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
admin.site.register(State, StateAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'project', 'due_date', 'state']
    list_filter = ['project', 'state']
    search_fields = ['title', 'description', 'due_date']
admin.site.register(Task, TaskAdmin)
