"""
URL configuration for ToDoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from apps.authentication.views import UserViewSet, CSRFTokenView
from apps.projects.views import StateViewSet, ProjectViewSet, TaskViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'states', StateViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='auth')),
    path('api/auth/csrf/', CSRFTokenView.as_view() , name='get-csrf-token'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
