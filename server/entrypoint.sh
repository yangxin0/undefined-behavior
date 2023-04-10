#!/bin/bash

export WORKERS=${SERVER_WORKERS:-3}
exec gunicorn chatgpt_proj.wsgi --workers=$WORKERS --timeout 60 --bind 0.0.0.0:8000 --access-logfile -
