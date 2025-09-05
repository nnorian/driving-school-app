# backend/catalog/models.py
from django.db import models
import uuid

class LessonCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class LessonPackage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(LessonCategory, on_delete=models.CASCADE, related_name="packages")
    title = models.CharField(max_length=100)
    num_lessons = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.num_lessons} lessons)"
