from django import forms
from django.core.validators import FileExtensionValidator


class CheckGrammarForm(forms.Form):
    file = forms.FileField(validators=[
        FileExtensionValidator(["md"], "Sólo se permiten archivos .md")
    ])
