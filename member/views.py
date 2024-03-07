from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone

from .forms import MembershipForm
from .models import Member, Attendance

# Create your views here.           

def home(request):
    attendance_count = Attendance.objects.filter(date=timezone.now().date(), status=True).count()
    first_timer_count = Member.objects.filter(status='First-Timer').count()
    total_member = Member.objects.count()

    
    context = {
        'attendance_count': attendance_count,
        'firsttimer_count': first_timer_count,
        'total_member': total_member,
    }
    return render(request, 'home.html', context)


def member_list(request):
    #get all member to display on html
    member = Member.objects.all()
    return render(request, 'member_list.html', {'member': member})

def member(request, pk):
    if request.user.is_authenticated:
        #Item lookup
        member = Member.objects.get(id=pk)
        return render(request, 'detailed_member.html', {'member':member}) 
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('member_list')
    
def delete_member(request, pk):
    if request.user.is_authenticated:
        delete_it = Member.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Item is deleted ...")
        return redirect('member_list')
    else:
        messages.success(request, "You are not authorised ...")
        return redirect('member_list')

def addmember(request):
    form = MembershipForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                addmember = form.save()
                messages.success(request, "Member is added ...")
                return redirect('member_list')
        return render(request, 'addmember.html', {'form':form})    
    else:
            messages.success(request, "You need to login ...")
            return redirect('member_list')         

def edit_member(request, pk):
    if request.user.is_authenticated:
        edit_it = Member.objects.get(id=pk)
        form = MembershipForm(request.POST or None, instance=edit_it)
        if form.is_valid():
            form.save()
            messages.success(request, "Member's record is updated ...")
            return redirect('member_list')
        return render(request, 'edit_member.html', {'form':form})    
    else:
        messages.success(request, "You need to login ...")
        return redirect('member_list')      

def attendance_list(request):
    #get all attendance records to display on html
    attendance = Attendance.objects.all()
    current_date = timezone.now().date()
    #attendance = Attendance.objects.filter(date=current_date).values_list('member__id', flat=True)
    #attendance = Member.objects.filter(attendance__status=True)  # Optimize query

    return render(request, 'attendance_list.html', {'attendance': attendance})

'''
def attendance(request):
    member = Member.objects.all()
    current_date = timezone.now().date()
    existing_attendance = Attendance.objects.filter(date=current_date).values_list('member__id', flat=True)
    
    if request.method == 'POST':
        for member in member:
            status = request.POST.get(str(member.id))
            if member.id in existing_attendance:
                attendance_record = Attendance.objects.get(member=member, date=current_date)
                attendance_record.status = (status == 'present')
                attendance_record.save()
            else:
                Attendance.objects.create(member=member, status=(status == 'present'), date=current_date)
        return redirect('attendance_summary')
    
    return render(request, 'addAttendance.html', {'member': member})
'''
def attendance(request):
    member = Member.objects.all()
    current_date = timezone.now().date()

    if request.method == 'POST':
        for member in member:
            status = request.POST.get(str(member.id))
            attendance, created = Attendance.objects.get_or_create(
                member=member, date=current_date, defaults={'status': (status == 'present')}
            )
            if not created:
                attendance.status = (status == 'present')
                attendance.save()

        return redirect('attendance_summary')

    return render(request, 'addAttendance.html', {'member': member})





def attendance_summary(request):
    present_count = Attendance.objects.filter(date=timezone.now().date(), status=True).count()
    context = {
        'present_count': present_count,
    }
    
    return render(request, 'attendance_summary.html', context)

  