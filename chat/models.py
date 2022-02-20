from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms

user = get_user_model()


class Chat(models.Model):
    roomname = models.CharField(blank=True, max_length=50)
    members = models.ManyToManyField(user, null=True, blank=True)

    def __str__(self):
        return self.roomname


class Message(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    content = models.TextField()
    related_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def last_message(self, roomname):
        return Message.objects.filter(related_chat__roomname=roomname)

    def __str__(self):
        return self.author.username


class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class Game(models.Model):
    game_time = models.DateTimeField()
    game_score = models.IntegerField()
    user = models.ForeignKey(User)
