# backend/reporting/models.py
from django.db import models
import uuid
from scheduling.models import Lesson

class LessonReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)  # student feedback 1-5 stars

    def __str__(self):
        return f"Report for {self.lesson}"

