from django.contrib import admin

from .models import Attendance, TotalAttendanceCount, Zone, Area, Hop, Member

admin.site.register(Attendance)
admin.site.register(TotalAttendanceCount)
admin.site.register(Zone)
admin.site.register(Area)
admin.site.register(Hop)
admin.site.register(Member)