"""
URL configuration for cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from member import views
""" #from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from member.views import MemberViewSet, AttendanceViewSet """


# Routers provide an easy way of automatically determining the URL conf.
""" router = DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'attendance', AttendanceViewSet) """


urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('', views.home, name='home'),
]
