#! /usr/bin/env python
import os
import sys
import django

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatgpt_proj.settings')
django.setup()

from chat.models import Setting

openai_sk = input('Input OpenAI Key: ')
print("Your OpenAI Key: '%s'" % (openai_sk))
Setting.objects.create(name='openai_api_key', value=openai_sk)
Setting.objects.create(name='open_registration', value='True')
Setting.objects.create(name='open_web_search', value='False')
Setting.objects.create(name='open_api_key_setting', value='False')

from django.contrib.auth.models import User
import uuid

password = str(uuid.uuid1()).replace('-', '')
User.objects.create_user(username="admin", password=password, 
                    is_superuser=True, is_staff=True, is_active=True)
print("Your admin account: admin/%s" % (password))
