# Generated by Django 5.0.2 on 2024-03-05 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('area_name', models.CharField(blank=True, max_length=50, null=True)),
                ('coordinator_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TotalAttendanceCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('total_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('zone_name', models.CharField(max_length=50)),
                ('zone_location', models.CharField(max_length=50)),
                ('zonal_head', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hop_name', models.CharField(blank=True, max_length=50, null=True)),
                ('leader_name', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.area')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('', ''), ('First-Timer', 'First-Timer'), ('NewComer', 'NewComer'), ('Member', 'Member')], max_length=50, null=True)),
                ('occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, choices=[('', ''), ('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('NPA_status', models.CharField(blank=True, choices=[('', ''), ('Completed', 'Completed'), ('Ready', 'Ready'), ('Ongoing', 'Ongoing'), ('Not-Ready', 'Not-Ready')], max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('', ''), ('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], max_length=50, null=True)),
                ('invited_by', models.CharField(blank=True, max_length=50, null=True)),
                ('day_to_be_visited', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.area')),
                ('attendance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.attendance')),
                ('hop', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.hop')),
                ('zone', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.zone')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.zone'),
        ),
    ]
