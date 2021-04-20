from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from .forms import UploadFileForm
from .models import *
from django.core.paginator import *
from datetime import datetime



# 기본페이지
def index(request):

    return render(request, 'page1.html')

def uploads(request) :
    if request.method == 'POST':

        # file = request.FILES['file'].read()
        print("test--------------------------------------")
        # file
        # print(file)

        name = request.POST.get('file','11')  # To get the name
        # size = request.POST.getlist('file','').size
        # type = request.POST.getlist('file','').content_type
        print("name-------",type(name),name)
    return render(request,'page1.html')

def upload_file(request):
    print('----------------------------------------------------------')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        name = form.name
        print('========name',name)
        if form.is_valid():
            form.save()
            print(form)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'page1.html', {'form': form})

# 음성서비스 페이지
def read(request):
    return render(request, 'page2.html')