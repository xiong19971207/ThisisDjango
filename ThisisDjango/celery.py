from __future__ import absolute_import, unicode_literals
from datetime import timedelta
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ThisisDjango.settings')

app = Celery('This')
# app.config_from_object('common.celery_config', namespace='CELERY')

# 从所有已注册的Django应用配置中加载任务模块。
app.autodiscover_tasks()

# 允许root 用户运行celery
# platforms.C_FORCE_ROOT = True


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))  # 原样输出

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y