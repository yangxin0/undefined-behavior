#! /usr/bin/env python
import os
import sys
import django

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatgpt_proj.settings')
django.setup()

from django.contrib.auth.models import User
from chat.models import Deposit, Balance

for user in User.objects.all():
    if Deposit.objects.filter(
            user=user, 
            source=Deposit.Source.TRIAL.name).count() >= 1:
        print("skip user: %s" % (user.get_username()))
        continue
    # 1$ free trial
    print("deposit $1 for %s" % (user.get_username()))
    Deposit.objects.create(user=user,
                           amount=1,
                           exchange=1,
                           source=Deposit.Source.TRIAL.name,
                           currency=Deposit.Currency.USD.name)
    Balance.objects.create(user=user, usd_amount=1)
