# Generated by Django 4.1.7 on 2023-02-22 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0008_recharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='Message',
            name='fees',
            field=models.IntegerField(default=0),
        ),
    ]

