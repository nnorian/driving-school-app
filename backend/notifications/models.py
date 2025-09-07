from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    type = models.CharField(max_length=50, default='general')
    channel = models.CharField(max_length=20, choices=[
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        ('PUSH', 'Push Notification'),], default='EMAIL')
    payload = models.JSONField(default=dict)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
