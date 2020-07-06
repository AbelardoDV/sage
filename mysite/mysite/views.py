from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import ArchivosCSV
import os
from django.template import RequestContext

def simple_upload_view(request):

    path = os.path.dirname(os.path.abspath(__file__))
    loc='mysite/static/files/'
    loc_f='../static/files/'
    # myfiles = os.path.join(path, loc)
    # os.chdir(myfiles)
    # x = 0
    # d = {}
    # for file in os.listdir("."):
    #     d[x] = (myfiles + file)
    #     x = x + 1

    # variables = RequestContext(request, {
    # 'user' : request.user,
    # 'filedict' : d,
    # })


    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=loc)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url =loc_f+ fs.url(filename)

        
        return render(request, 'pages/simple_upload.html', locals())
    return render(request, 'pages/simple_upload.html', locals())