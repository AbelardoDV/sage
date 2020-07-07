from django.core.files.storage import FileSystemStorage
from django.db import models

loc='mysite/static/files/'
fs = FileSystemStorage(location=loc)

