from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Setting

@receiver(post_migrate)
def load_default_settings(sender, **kwargs):
    pass
