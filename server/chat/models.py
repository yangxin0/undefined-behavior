from django.db import models
from django.contrib.auth.models import User

class Recharge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=255)
    total_token_num = models.IntegerField(default=0)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message = models.TextField()
    is_bot = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    total_token_num = models.IntegerField(default=0)
    fees = models.FloatField(default=0)

class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Setting(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
