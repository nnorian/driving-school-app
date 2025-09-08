from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class School(models.Model):
    name = models.CharField(max_length=255)
    timezone = models.CharField(max_length=64, default="Europe/Chisinau")
    contact_info = models.TextField(blank=True, null=True)
    settings = models.JSONField(default=dict, blank=True)

    def __str__(self): 
        return self.name

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    ROLE_STUDENT = "STUDENT"
    ROLE_INSTRUCTOR = "INSTRUCTOR"
    ROLE_DIRECTOR = "DIRECTOR"
    ROLE_ADMIN = "ADMIN"
    ROLE_CHOICES = [
        (ROLE_STUDENT, "Student"),
        (ROLE_INSTRUCTOR, "Instructor"),
        (ROLE_DIRECTOR, "Director"),
        (ROLE_ADMIN, "Admin"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=30, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    notification_prefs = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.email} ({self.role})"

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    selected_categories = models.ManyToManyField("catalog.LessonCategory", blank=True)
    packages = models.ManyToManyField("catalog.LessonPackage", blank=True)
    preferences = models.JSONField(default=dict, blank=True)

class InstructorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="instructor_profile")
    qualifications = models.TextField(blank=True)
    permitted_categories = models.ManyToManyField("catalog.LessonCategory", blank=True)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
