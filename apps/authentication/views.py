from django.shortcuts import render
from django.contrib.auth.models import User
from django.middleware.csrf import get_token

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializer import UserSerializer


# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser] ## Solo los usuarios administradores pueden acceder a este endpoint
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class CSRFTokenView(APIView):
    permission_classes = [AllowAny]  # Indica que no se requieren permisos
    
    def get(self, request, *args, **kwargs):
        # obtener el token CSRF
        csrf_token = get_token(request)
        
        # Devuelve el token como respuesta
        return Response(data={'csrf_token': csrf_token}, status=200)