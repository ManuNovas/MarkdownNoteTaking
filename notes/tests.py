from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class CheckGrammarTests(TestCase):
    def test_check_grammar_success(self):
        note = SimpleUploadedFile("test.md", b"# Este es un archivo de prueba")
        response = self.client.post(reverse("notes:check-grammar"), {"file": note})
        self.assertEqual(response.status_code, 200)

    def test_check_grammar_without_file(self):
        response = self.client.post(reverse("notes:check-grammar"))
        self.assertEqual(response.status_code, 400)

    def test_check_grammar_with_invalid_file(self):
        note = SimpleUploadedFile("test.txt", b"This is a test file")
        response = self.client.post(reverse("notes:check-grammar"), {"file": note})
        self.assertEqual(response.status_code, 400)


class SaveTests(TestCase):
    def test_save_success(self):
        note = SimpleUploadedFile("test.md", b"# Este es un archivo de prueba")
        response = self.client.post(reverse("notes:save"), {"file": note})
        self.assertEqual(response.status_code, 200)

    def test_save_without_file(self):
        response = self.client.post(reverse("notes:save"))
        self.assertEqual(response.status_code, 400)

    def test_save_with_invalid_file(self):
        note = SimpleUploadedFile("test.txt", b"This is a test file")
        response = self.client.post(reverse("notes:save"), {"file": note})
        self.assertEqual(response.status_code, 400)
