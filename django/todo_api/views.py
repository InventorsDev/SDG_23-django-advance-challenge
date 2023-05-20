from datetime import datetime


from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)


from todo_api.models import Task
from todo_api.serializers import (
    TaskSerializer,
    TaskCreateSerializer,
    TaskUpdateSerializer,
)


class TaskGetCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        due_date = request.query_params.get("due_date", None)
        status = request.query_params.get("status", None)
        title = request.query_params.get("title", None)

        base_query = Task.objects.all()
        filtered_task = base_query

        if status:
            filtered_task = base_query.filter(status=status)

        if title:
            filtered_task = base_query.filter(title__icontains=title)

        if due_date:
            filtered_task = base_query.filter(due_date__date=due_date)

        all_task_data = TaskSerializer(filtered_task, many=True).data

        return Response(data=all_task_data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        form = TaskCreateSerializer(data=request.data)

        if form.is_valid():
            task_data = form.save()

            return Response(task_data, status=HTTP_201_CREATED)

        return Response(form.errors, status=HTTP_400_BAD_REQUEST)


class TaskSingleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, task_id, *args, **kwargs):
        task = Task.objects.filter(id=task_id).first()

        if task is None:
            context = {"message": "Task not found"}
            return Response(context, status=HTTP_404_NOT_FOUND)

        task_data = TaskSerializer(task).data

        return Response(task_data, status=HTTP_200_OK)

    def patch(self, request, task_id, *args, **kwargs):
        task = Task.objects.filter(id=task_id).first()

        if task is None:
            context = {"message": "Task not found"}
            return Response(context, status=HTTP_404_NOT_FOUND)

        form = TaskUpdateSerializer(data=request.data)

        if form.is_valid():
            task_data = form.update(current_task=task)

            return Response(task_data, status=HTTP_200_OK)

        context = {"message": "Validation errors", "errors": form.errors}

        return Response(context, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, *args, **kwargs):
        task = Task.objects.filter(id=task_id).first()

        if task is None:
            context = {"message": "Task not found"}
            return Response(context, status=HTTP_404_NOT_FOUND)

        task.delete()

        return Response(status=HTTP_204_NO_CONTENT)


class TaskMarkCompletedView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request, task_id, *args, **kwargs):
        task = Task.objects.filter(id=task_id).first()

        if task is None:
            context = {"message": "Task not found"}
            return Response(context, status=HTTP_404_NOT_FOUND)

        task.status = "completed"
        task.save()

        task_data = TaskSerializer(task).data

        return Response(task_data, status=HTTP_200_OK)
