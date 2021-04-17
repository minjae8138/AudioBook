from django.http import JsonResponse
from django.shortcuts import render , redirect
from .models import *
from django.core.paginator import *
from datetime import datetime
from django.db.models import Max, functions
from django.core.paginator import Paginator
from django.db.models import Aggregate, CharField
from django.db.models import Sum, F

def index(request):

    return render(request, 'page1.html')
