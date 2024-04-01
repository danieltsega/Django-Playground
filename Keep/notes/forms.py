from django import forms

from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2 bg-slate-200',
        'placeholder': 'Add your note title here...'
    }), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'h-64 w-full border rounded focus:outline-none py-3 px-3 text-gray-700 mt-2 bg-slate-200',
        'placeholder': 'Write your note here...'
    }), label='')
    
    class Meta:
        model = Note
        fields = ['title', 'description']