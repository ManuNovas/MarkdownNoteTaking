from django.urls import path

from notes.views import check_grammar, save, read

app_name = "notes"
urlpatterns = [
    path("check-grammar", check_grammar, name="check-grammar"),
    path("save", save, name="save"),
    path("read", read, name="read"),
]
