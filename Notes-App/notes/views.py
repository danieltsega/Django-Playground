from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

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

class DeleteNoteView(DeleteView):
    model = Note
    success_url = reverse_lazy('home')
    template_name = "index.html"

class UpdateNoteView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "add_note.html"
    success_url = reverse_lazy("home")
    
class DetailNoteView(DetailView):
    model = Note
    template_name = "detail_note.html"