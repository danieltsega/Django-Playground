from django.urls import path

from .views import index, delete_task, completed, edit_task

urlpatterns = [
    path("", index, name="home"),
    #path("add-task/", add_task, name="add-task"),
    path("delete-task/<int:task_id>/", delete_task, name="delete-task"),
    path("completed/<int:task_id>", completed, name="completed"),
    path("edit-task/<int:task_id>/", edit_task, name="edit-task")
]
