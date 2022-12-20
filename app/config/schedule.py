from datetime import timedelta
from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
   'strategy_rules_base': {
       'task': 'resolve_strategy',
       'schedule': timedelta(minutes=30),
   },
}