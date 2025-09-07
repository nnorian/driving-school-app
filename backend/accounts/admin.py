from django.contrib import admin
from .models import User, School, StudentProfile, InstructorPRofile

# Register your models here.
admin.site.register(School)
admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(InstructorProfile)