from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    action_type = models.CharField(max_length=100)
    target_type = models.CharField(max_length=100, null=True)
    target_id = models.PositiveIntegerField(null=True)
    details = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
