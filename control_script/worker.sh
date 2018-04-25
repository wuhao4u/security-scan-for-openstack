#!/bin/sh

ps -ef | grep celery | awk '{print $2}' | xargs kill -9
#cd /home/ubuntu/Security-Scan-for-OpenStack && /home/ubuntu/.local/bin/celery worker -l info -A my_celery.tasks --concurrency=1
