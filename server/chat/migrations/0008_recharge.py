# Generated by Django 4.1.7 on 2023-02-22 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0007_add_total_token_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0)),
            ],
        ),
    ]

