from django.shortcuts import render
from django.db.models import Q

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from .models import State, Project, Task
from .serializer import StateSerializer, ProjectSerializer, TaskSerializer


# Create your views here.
# ViewSets define the view behavior.

class StateViewSet(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
  queryset = State.objects.all()
  serializer_class = StateSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  pagination_class = PageNumberPagination
  
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['user']
  search_fields = ['name']
  ordering_fields = ['name', 'user']
  
  def get_queryset(self):
        queryset = super().get_queryset()
        
        ## Filtrar los proyectos siempre por el usuario en sesion
        queryset = Project.objects.filter(user=self.request.user)
        
        return queryset

class TaskViewSet(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  pagination_class = PageNumberPagination
  
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['project', 'state']
  search_fields = ['title']
  ordering_fields = ['title', 'project', 'state', 'due_date']
  
  def get_queryset(self):
        queryset = super().get_queryset()
        
        ## Filtrar las tareas siempre por el usuario en sesion del proyecto
        queryset = Task.objects.filter(project__user__id=self.request.user.id)
        
        return queryset