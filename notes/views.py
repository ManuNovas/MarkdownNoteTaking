from django.http import JsonResponse, HttpResponse
from language_tool_python import LanguageTool
from markdown import markdown

from notes.forms import NoteForm
from notes.models import Note


# Create your views here.
def check_grammar(request):
    try:
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data['file'].read().decode('utf-8')
            tool = LanguageTool("es-MX")
            matches = tool.check(content)
            tool.close()
            json = {
                "check": True,
                "errors": []
            }
            if len(matches) > 0:
                json["check"] = False
                for match in matches:
                    json["errors"].append({
                        "rule_id": match.ruleId,
                        "message": match.message,
                        "offset": match.offset,
                        "length": match.errorLength,
                        "replacements": match.replacements,
                        "context": match.context,
                        "sentence": match.sentence,
                    })
            response = JsonResponse(json, safe=False)
        else:
            response = JsonResponse({'errors': form.errors}, status=400)
    except Exception as e:
        print(e)
        response = JsonResponse({'message': 'Ocurrió un error al revisar la grámatica'}, status=500)
    return response


def save(request):
    try:
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = Note(file=form.files['file'])
            note.save()
            response = JsonResponse(note.serialize(), status=200)
        else:
            response = JsonResponse({'errors': form.errors}, status=400)
    except Exception as e:
        print(e)
        response = JsonResponse({
            "message": "Ocurrió un error al guardar la nota"
        }, status=500)
    return response


def read(request):
    try:
        notes = Note.objects.all()
        json = [note.serialize() for note in notes]
        response = JsonResponse(json, safe=False)
    except Exception as e:
        print(e)
        response = JsonResponse({
            "message": "Ocurrió un error al listar las notas"
        }, status=500)
    return response


def parse(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
        content = note.file.read().decode('utf-8')
        html = markdown(content)
        response = HttpResponse(html)
    except Exception as e:
        print(e)
        response = HttpResponse("Ocurrió un error al parsear la nota", status=500, content_type="text/plain")
    return response
