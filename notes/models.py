from django.db import models

# Create your models here.
class Note(models.Model):
    file = models.FileField(upload_to="notes/storage/")

    def serialize(self):
        return {
            "id": self.id,
            "file": self.file.url
        }
