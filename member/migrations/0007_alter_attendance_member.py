# Generated by Django 5.0.2 on 2024-03-05 22:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_attendance_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='member',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
    ]
