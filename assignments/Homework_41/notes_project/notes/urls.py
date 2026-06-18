from django.urls import path

from .views import (
    home,
    create_note,
    note_detail,
    edit_note,
    delete_note
)

urlpatterns = [
    path("", home, name="home"),

    path(
        "create/",
        create_note,
        name="create_note"
    ),

    path(
        "note/<int:pk>/",
        note_detail,
        name="note_detail"
    ),

    path(
        "note/<int:pk>/edit/",
        edit_note,
        name="edit_note"
    ),

    path(
        "note/<int:pk>/delete/",
        delete_note,
        name="delete_note"
    ),
]