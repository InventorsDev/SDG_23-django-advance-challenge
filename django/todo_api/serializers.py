from rest_framework import serializers

from todo_api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    due_date = serializers.DateTimeField(required=False)
    description = serializers.CharField(required=False, default="")

    def save(self):
        new_task = Task()
        new_task.title = self.validated_data["title"].title()
        new_task.due_date = self.validated_data.get("due_date")
        new_task.description = self.validated_data.get("description")
        new_task.status = "uncompleted"
        new_task.save()

        task_data = TaskSerializer(new_task).data

        return task_data


class TaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    due_date = serializers.DateTimeField(required=False)
    description = serializers.CharField(required=False, default="")
    status = serializers.ChoiceField(
        choices=["completed", "uncompleted"], required=False
    )

    def update(self, current_task: Task):
        current_task.title = self.validated_data.get("title", current_task.title)
        current_task.due_date = self.validated_data.get(
            "due_date", current_task.due_date
        )
        current_task.description = self.validated_data.get(
            "description", current_task.description
        )
        current_task.status = self.validated_data.get("status", current_task.status)
        current_task.save()

        task_data = TaskSerializer(current_task).data

        return task_data
