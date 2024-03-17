from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    task = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 w-full border rounded focus:outline-none py-3 px-3 text-gray-700  mr-2',
        'placeholder': 'Enter your task here...'
    }), label='')
    class Meta:
        model = Task
        fields = ['task']