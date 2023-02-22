from rest_framework import serializers

from managment_system.users.api.serializers import UserSerializer

from managment_system.tasks.models import Team, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
            "completed",
            "creator",
            "assignee",
        ]

    def get_creator(self, obj):
        return obj.creator.username

    def get_assignee(self, obj):
        return obj.assignee.username

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            "id",
            'name',
            'member',
        ]

    
    #def get_tasks(self, obj):
        #tasks = Task.objects.filter(team=obj)
        #task_serializer = TaskSerializer(tasks, many=True)
        #return task_serializer.data