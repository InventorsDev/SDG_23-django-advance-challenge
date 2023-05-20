from django.urls import path

from todo_api.views import TaskGetCreateView, TaskMarkCompletedView, TaskSingleView

urlpatterns = [
    path("tasks", TaskGetCreateView.as_view(), name="task_list"),
    path("tasks/<int:task_id>", TaskSingleView.as_view(), name="task_detail"),
    path(
        "tasks/<int:task_id>/completed",
        TaskMarkCompletedView.as_view(),
        name="task_complete",
    ),
]
