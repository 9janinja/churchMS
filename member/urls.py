from django.urls import path
from . import views
from .views import MemberViewSet, AttendanceViewSet


from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'attendance', AttendanceViewSet)


urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('<int:pk>', views.member, name='member'),
    path('delete/<int:pk>', views.delete_member, name='delete_member'),
    path('add/', views.addmember, name='addmember'),
    path('edit/<int:pk>', views.edit_member, name='edit'),
    path('', include(router.urls)),
    #path('threading_example', ctviews.ThreadingExampleView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #path('attendance_list/', views.attendance_list, name='attendance_list'),
    #path('attendance/', views.attendance, name='attendance'),
    #path('summary/', views.attendance_summary, name='attendance_summary'),
]