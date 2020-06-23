from django.contrib.auth.models import User
from django.db import models


class Medicine(models.Model):
    id = models.IntegerField(primary_key=True)
    local = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='created_medicines')
    users = models.ManyToManyField(User, through='ScheduleRow')


class DoseVariant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    doses_per_day = models.IntegerField()
    dose_size_description = models.CharField(max_length=1048)
    dose_interval = models.DurationField()
    course_interval = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)


class ScheduleRow(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
