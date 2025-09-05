# backend/scheduling/models.py
from django.db import models
import uuid
from accounts.models import User
from catalog.models import LessonCategory

class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_lessons", limit_choices_to={"role": "student"})
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructor_lessons", limit_choices_to={"role": "instructor"})
    category = models.ForeignKey(LessonCategory, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ], default="scheduled")

    def __str__(self):
        return f"{self.student} with {self.instructor} on {self.start_time}"
