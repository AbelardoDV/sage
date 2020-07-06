from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import ArchivosCSV
import os
from django.template import RequestContext
from pathlib import Path

def simple_upload_view(request):

    
    loc='mysite/static/files/'
    loc_f='../static/files/'
    
    
    #################
    path = Path(r"D:\\eica\\covid\\sage\\mysite\\static\\files")
    files_in_path = path.iterdir()
    list_files=[]
    for item in files_in_path:
        if item.is_file():
            list_files.append(item.name)

    #################


    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=loc)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url =loc_f+ fs.url(filename)

        
        return render(request, 'pages/simple_upload.html', locals())
    return render(request, 'pages/simple_upload.html', locals())