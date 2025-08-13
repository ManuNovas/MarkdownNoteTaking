from django.urls import path

from notes.views import check_grammar

app_name = "notes"
urlpatterns = [
    path("check-grammar", check_grammar, name="check-grammar")
]
