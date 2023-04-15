from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usd_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class DespoitSource(Enum):
    WECHAT = "Wechat"
    TRIAL = "Trial"

class DespoitCurrency(Enum):
    USD = "USD"
    RMB = "RMB"
    EUR = "EUR"

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0) # currency value
    exchange = models.FloatField(default=1) # default exhange rate for usd
    source = models.CharField(max_length=255, default="Trial",
                              choices=[(t, t.value) for t in DespoitSource])
    currency = models.CharField(max_length=255, default="USD",
                                choices=[(t, t.value) for t in DespoitCurrency])
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255, default='gpt-3.5-turbo')
    total_token = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message = models.TextField()
    is_bot = models.BooleanField(default=False) # user prompt or GPT answer(is_bot=1)
    total_token = models.IntegerField(default=0)
    usd_cost = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class MessageCost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    usd_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Setting(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
