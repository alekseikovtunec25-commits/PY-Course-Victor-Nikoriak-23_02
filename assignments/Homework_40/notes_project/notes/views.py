from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Note


def home(request):
    notes = Note.objects.select_related('category').all()
    return render(request, 'home.html', {'notes': notes})