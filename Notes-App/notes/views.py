from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Note
from .forms import NoteForm

# Create your views here.
class ListNoteView(ListView):
    model = Note
    template_name = "index.html"


class CreateNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "add_note.html"
    success_url = reverse_lazy('home')