
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Team(models.Model):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField(User, related_name='teams')
    
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField('Название', max_length=200, db_index=True)
    description = models.TextField('Описание', blank=True, null=True)
    created_at = models.DateTimeField('Дата_создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата_последнего_обновления', auto_now=True)
    completed = models.BooleanField('Оконченность_задачи', default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
