from django import forms
from django.core.validators import FileExtensionValidator


class NoteForm(forms.Form):
    file = forms.FileField(validators=[
        FileExtensionValidator(["md"], "Sólo se permiten archivos .md")
    ])
