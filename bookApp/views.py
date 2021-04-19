from django.http import JsonResponse
from django.shortcuts import render , redirect
from .models import *

# 테스트용도
def test(request):
    users = UserTb.objects.all()
    for user in users:
        print(user.user_id)
        print(user.name)
    return render(request, 'test.html', {'posts':users})



# 기본페이지
def index(request):

    return render(request, 'page1.html')

# 음성서비스 페이지

