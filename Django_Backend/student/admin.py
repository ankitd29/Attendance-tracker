from django.contrib import admin
from .models import Pupil, Attendance

# Register your models here.
admin.site.register(Pupil)
admin.site.register(Attendance)