from __future__ import absolute_import
from celery import Celery

app = Celery('my_celery',
             broker='amqp://jimmy:jimmy123@10.0.0.6/jimmy_vhost',
             backend='rpc://',
             include=['my_celery.tasks'])
