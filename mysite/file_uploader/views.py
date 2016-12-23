from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import UploadFileForm


def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid(): #Kiem tra tinh hop le du lieu gui len
            upload(request.FILES['file'])
            return HttpResponse("<h2>File uploaded successful!</h2>")
        else:
            return HttpResponse("<h2>File uploaded not successful!</h2>")

    form = UploadFileForm()
    return render(request, 'fileUploadTemplate.html', {'form': form})

#thực hiện copy file vào thư mục gốc của server (thư mục có file manage.py).
def upload(f):
    file = open(f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
