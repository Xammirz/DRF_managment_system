import os

from celery import Celery, shared_task

from django.core.mail import send_mail
# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("managment_system")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@shared_task
def send_mail_tasks(recipient):

    send_mail(
        subject="New Tasks",
        message="New Task",
        from_email='ramzanxam@gmail.com',
        recipient_list=[recipient],
        fail_silently=False,
    )