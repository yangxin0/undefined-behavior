from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Deposit, Balance
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def handle_user_post_save(sender, instance, created, **kwargs):
    if created == False:
        return
    # 1$ free trial
    Deposit.objects.create(user=instance,
                           amount=1,
                           exchange=1,
                           source=Deposit.Source.TRIAL.name,
                           currency=Deposit.Currency.USD.name)
    Balance.objects.create(user=instance, usd_amount=1)
