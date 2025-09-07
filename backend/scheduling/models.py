from django.db import models
from django.conf import settings
from accounts.models import School
from catalog.models import LessonCategory

class InstructorAvailability(models.Model):
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="availabilities")
    day_of_week = models.IntegerField(null=True, blank=True)  
    date = models.DateField(null=True, blank=True)       
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_recurring = models.BooleanField(default=True)

class Lesson(models.Model):
    STATUS_SCHEDULED = "SCHEDULED"
    STATUS_CANCELLED = "CANCELLED"
    STATUS_COMPLETED = "COMPLETED"
    STATUS_CHOICES = [
        (STATUS_SCHEDULED, "Scheduled"),
        (STATUS_CANCELLED, "Cancelled"),
        (STATUS_COMPLETED, "Completed"),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    category = models.ForeignKey(LessonCategory, on_delete=models.PROTECT)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lessons_as_instructor")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lessons_as_student")
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_SCHEDULED)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="created_lessons", on_delete=models.SET_NULL)
    canceled_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="canceled_lessons", on_delete=models.SET_NULL)
    cancel_reason = models.TextField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
