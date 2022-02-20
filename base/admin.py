from django.contrib import admin

from .models import Blog, Workout, Plan

# Register your models here.
admin.site.register(Blog)
admin.site.register(Workout)
admin.site.register(Plan)