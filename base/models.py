from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    create = models.DateTimeField(auto_now_add=True)
    #views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-create']




class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create']

class Workout(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    gif = models.TextField(null=True,blank=True)
    equipment = models.CharField(max_length=200, null=True, blank=True)
    log = [2, 3, 4]
