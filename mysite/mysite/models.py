from django.core.files.storage import FileSystemStorage
from django.db import models

loc='mysite/static/files/'
fs = FileSystemStorage(location=loc)


class ArchivosCSV(models.Model):

    IdFile=models.IntegerField(primary_key=True)
    photo = models.ImageField(storage=fs)
    
    def __str__(self):
        return self.name    