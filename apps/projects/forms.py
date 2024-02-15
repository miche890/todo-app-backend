from django import forms
from django.contrib.auth.models import Group, User


from .models import Project

class ProjectForm(forms.ModelForm):
  
  class Meta:
    model = Project
    fields =  '__all__'
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if Group.objects.filter(name__iexact='Usuarios').exists():
      group = Group.objects.get(name__iexact='Usuarios')
      self.fields['user'].queryset = group.user_set.all().order_by('username')
    else:
      self.fields['user'].queryset = User.objects.none()