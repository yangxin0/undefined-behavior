# Generated by Django 4.1.7 on 2023-04-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_conversation_model_name_conversation_total_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='usd_amount',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='billing_rule',
            field=models.FloatField(choices=[(3e-06, 'TENOPENAI'), (3e-07, 'OPENAI')], default=3e-06),
        ),
    ]
