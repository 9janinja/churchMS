from django.db import models

# Create your models here.
class Zone(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    zone_name = models.CharField(max_length=50)
    zone_location = models.CharField(max_length=50)
    zonal_head = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.zone_name}'
    
class Area(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    area_name = models.CharField(max_length=50, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    coordinator_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.area_name}'  

class Hop(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    hop_name = models.CharField(max_length=50, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    leader_name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f'{self.hop_name}'


""" class Member(models.Model):

    STATUS = (
        ('',''),
        ('First-Timer', 'First-Timer'),
        ('NewComer', 'NewComer'),
        ('Member', 'Member'),
    )
    SEX = (
        ('',''),
        ('Male', 'Male'),
        ('Female','Female'),
    )

    NPA = (
        ('',''),
        ('Completed', 'Completed'),
        ('Ready', 'Ready'),
        ('Ongoing', 'Ongoing'),
        ('Not-Ready', 'Not-Ready'),
    )
    MARITAL = (
        ('',''),
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS)

    hop = models.ForeignKey(Hop, on_delete=models.CASCADE, default=None, null=True, blank=True,)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=None, null=True, blank=True,)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, default=None, null=True, blank=True,)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True, choices=SEX)
    NPA_status = models.CharField(max_length=50, null=True, blank=True, choices=NPA)
    marital_status = models.CharField(max_length=50, null=True, blank=True, choices=MARITAL)
    invited_by = models.CharField(max_length=50, null=True, blank=True)
    day_to_be_visited = models.CharField(max_length=50, null=True, blank=True)

    remarks = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True,)
    
    def __str__(self):
        return f'{self.first_name } {self.last_name}'

class Attendance(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=None, null=True, blank=True)
    #member = models.ForeignKey(Member, on_delete=models.CASCADE, unique=True, default=None, null=True, blank=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE, default=None, null=True, blank=True)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.date}" """
   
class TotalAttendanceCount(models.Model):
    date = models.DateField(unique=True)
    total_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Total Attendance Count: {self.total_count}"
    

class Member(models.Model):
    #name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    perfect_attendance = models.BooleanField(default=True, null=True, blank=True)  # True if attended all classes.
    # perfect attendance automatically becomes false if student is not present on any day.
    # it does not auto update to True if all attendance entries are updated to True
    # but setting it as false it automatic


class Attendance(models.Model):
    student = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.present:
            student = Member.objects.get(id=self.student.id)
            student.perfect_attendance = False
            student.save()
        super(Attendance, self).save(*args, **kwargs)