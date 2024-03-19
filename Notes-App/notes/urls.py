from django.urls import path

from .views import index, CreateNoteView

urlpatterns = [
    path("", index, name="home"),
    path("add-note", CreateNoteView.as_view(), name="add-note")
]
