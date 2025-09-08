from django.contrib import admin
from .models import LessonCategory, LessonPackage

# Register your models here.
admin.site.register(LessonCategory)
admin.site.register(LessonPackage)
