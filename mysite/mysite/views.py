from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os
from django.template import RequestContext
from pathlib import Path

def simple_upload_view(request):

    
    loc='mysite/static/files/'
    loc_f='../static/files/'
    
    # files_static_folder=os.path.dirname(os.path.abspath(loc))
    # print(files_static_folder)
    
    #################
    path = Path(r'D:\\SharkTank\\ManagementPlatform\\mysite\\static\\files\\')
    files_in_path = path.iterdir()
    list_files=[]
    for item in files_in_path:
        if item.is_file():
            list_files.append(item.name)

    #################


    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='D:\\SharkTank\\ManagementPlatform\\mysite\\static\\files\\')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url =loc_f+ fs.url(filename)

        
        return render(request, 'pages/simple_upload.html', locals())
    return render(request, 'pages/simple_upload.html', locals())