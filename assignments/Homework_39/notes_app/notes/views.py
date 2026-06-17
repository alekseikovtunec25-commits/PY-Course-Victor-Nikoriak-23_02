from django.shortcuts import render

def index(request):
    notes = [
        {"title": "Заметка 1", "text": "Купить хлеб"},
        {"title": "Заметка 2", "text": "Изучить Django"},
    ]
    return render(request, "notes/index.html", {"notes": notes})