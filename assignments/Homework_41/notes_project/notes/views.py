from django.shortcuts import render

# Create your views here.
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Note
from .forms import NoteForm


def home(request):

    notes = Note.objects.all()

    return render(
        request,
        "notes/home.html",
        {"notes": notes}
    )


def create_note(request):

    if request.method == "POST":

        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("home")

    else:
        form = NoteForm()

    return render(
        request,
        "notes/create_note.html",
        {"form": form}
    )


def note_detail(request, pk):

    note = get_object_or_404(
        Note,
        pk=pk
    )

    return render(
        request,
        "notes/note_detail.html",
        {"note": note}
    )


def edit_note(request, pk):

    note = get_object_or_404(
        Note,
        pk=pk
    )

    if request.method == "POST":

        form = NoteForm(
            request.POST,
            instance=note
        )

        if form.is_valid():
            form.save()

            return redirect(
                "note_detail",
                pk=note.pk
            )

    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "notes/edit_note.html",
        {
            "form": form,
            "note": note
        }
    )


def delete_note(request, pk):

    note = get_object_or_404(
        Note,
        pk=pk
    )

    if request.method == "POST":

        note.delete()

        return redirect("home")

    return render(
        request,
        "notes/delete_note.html",
        {"note": note}
    )