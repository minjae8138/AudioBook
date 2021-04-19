from django.http import JsonResponse
from django.shortcuts import render , redirect
from .models import *
from django.core.paginator import *
from datetime import datetime
from django.db.models import Max, functions
from django.core.paginator import Paginator
from django.db.models import Aggregate, CharField
from django.db.models import Sum, F


# 기본페이지
def index(request):

    return render(request, 'page1.html')

# 음성서비스 페이지
def read(request):
    return render(request, 'page2.html')