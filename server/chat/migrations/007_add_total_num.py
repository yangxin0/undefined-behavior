# Generated by Django 4.1.7 on 2023-03-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0006_add_prompt_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='Message',
            name='total_token_num',
            field=models.IntegerField(default=0),
        ),
    ] 