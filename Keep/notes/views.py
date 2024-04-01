from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Note
from .forms import NoteForm

from django.urls import reverse_lazy

# Create your views here.
class ListNoteView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'index.html'
    
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    
class CreateNoteView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'add_note.html'
    success_url = reverse_lazy('home')
    
class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('home')
    template_name = "index.html"

class UpdateNoteView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "add_note.html"
    success_url = reverse_lazy("home")
    
class DetailNoteView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "detail_note.html"