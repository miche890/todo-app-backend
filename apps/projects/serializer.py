from rest_framework import serializers

from .models import State, Project, Task

# Serializers define the API representation.

# Serializers define the API representation.
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Project
    fields = '__all__'

class TaskSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'