# backend/accounts/models.py
from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Django will handle hashing
    role = models.CharField(max_length=50, choices=[
        ("student", "Student"),
        ("instructor", "Instructor"),
        ("director", "Director"),
        ("admin", "Admin"),
    ])
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"
