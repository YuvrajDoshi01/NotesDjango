import email
from time import time
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.


class Note(models.Model):
    title = models.TextField(max_length=256)
    tags = models.TextField(max_length=256)
    body = models.TextField(max_length=512)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,null = True , blank=True)
    time_added = models.TimeField(auto_now_add= True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    
