from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Note
from .forms import NoteForm

# Create your views here.

def index(request):
    return render(request, "index.html", {})

class CreateNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "add_note.html"
    success_url = reverse_lazy('home')