from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('<int:pk>', views.member, name='member'),
    path('delete/<int:pk>', views.delete_member, name='delete_member'),
    path('add/', views.addmember, name='addmember'),
    path('edit/<int:pk>', views.edit_member, name='edit'),
    path('attendance_list/', views.attendance_list, name='attendance_list'),
    path('attendance/', views.attendance, name='attendance'),
    path('summary/', views.attendance_summary, name='attendance_summary'),
]