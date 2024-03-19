from django.urls import path

from .views import ListNoteView, CreateNoteView, DeleteNoteView, UpdateNoteView

urlpatterns = [
    path("", ListNoteView.as_view(), name="home"),
    path("add-note", CreateNoteView.as_view(), name="add-note"),
    path("delete-note/<int:pk>/", DeleteNoteView.as_view(), name="delete-note"),
    path("edit-note/<int:pk>", UpdateNoteView.as_view(), name="edit-note")
]
