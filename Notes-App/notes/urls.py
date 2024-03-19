from django.urls import path

from .views import ListNoteView, CreateNoteView

urlpatterns = [
    path("", ListNoteView.as_view(), name="home"),
    path("add-note", CreateNoteView.as_view(), name="add-note")
]
