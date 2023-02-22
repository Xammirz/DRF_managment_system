from rest_framework import viewsets

from django.dispatch import receiver
from django.db.models.signals import post_save

from managment_system.tasks.api.serializers import TeamSerializer, TaskSerializer
from managment_system.tasks.models import Team, Task
from config.celery_app import send_mail_tasks

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related('member')
    serializer_class = TeamSerializer
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('creator', 'assignee')
    serializer_class = TaskSerializer

    @receiver(post_save, sender=Task)
    def send_email_on_create(sender, instance, created, **kwargs):
        if created:
            send_mail_tasks.delay(instance.assignee.email)
