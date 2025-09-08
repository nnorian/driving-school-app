from django.db import models
from accounts.models import School

class LessonCategory(models.Model):
    code = models.CharField(max_length=10,  blank=True, default='')
    name = models.CharField(max_length=255)
    default_duration_minutes = models.IntegerField(default=90)
    description = models.TextField(blank=True)

    def __str__(self): 
        return f"{self.code} - {self.name}"

class LessonPackage(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="packages", null=True, blank=True)
    categories = models.ManyToManyField(LessonCategory, blank=True)
    number_of_hours = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
