from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from .models import *

# 파이썬
import re
import pandas as pd
import numpy as np

# 모델
from konlpy.tag import Komoran
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model







# 테스트용도
def test(request):
    users = UserTb.objects.all()
    for user in users:
        print(user.user_id)
        print(user.name)
    return render(request, 'test.html', {'posts':users})


# 모델로드 및 세팅
model = load_model('nlp_model.h5')
tokenizer = Tokenizer()
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
kor = Komoran()

# 기본페이지
def index(request):

    return render(request, 'page1.html')

# 리스트형식 개행제거 함수
def del_useless(text_list, del_list):
    for i in del_list:
        while True:
            try :
                text_list.remove(i)
            except :
                break
    return text_list

# 업로드된 텍스트파일을 모델에 적용하는 로직
def pred(test_file):
    for i in range(len(test_file)):
        if len(test_file[i].lstrip()) == 0:
            pass
        else:
            new_sentence = kor.morphs(test_file[i])
            new_sentence = [word for word in new_sentence if not word in stopwords]
            tokenizer.fit_on_texts(new_sentence)
            encoded = tokenizer.texts_to_sequences([new_sentence])
            # print(encoded)
            pad_new = pad_sequences(encoded, maxlen=30)
            y_pred = model.predict_classes(pad_new, verbose=1)
            # print("-------------------------------")
            # print(y_pred)
            # print('-------------------------------')
            test_file[i] = "".join(test_file[i]) + str(y_pred)
            # print(test_file[i])
            # print("------", test_file[i][-2])

    return test_file

# 파일 업로드
def upload(request) :
    file = request.FILES['text']
    # print('request upload - ',file)

    # 디코딩 작업 - 현재는 utf-8 형식의 txt파일만 업로드 가능, ansi 형식 고려x
    result_file=file.read().decode('utf-8')

    # 괄호 처리
    regex_gualho = '\([^)]*\)'
    r_cont = re.sub(regex_gualho, '', result_file)

    # 개행 제거
    r_cont = re.sub("\n", "", r_cont)
    mid = re.split('[".]', r_cont)
    fin_list = del_useless(mid, ['', ' ', '  ' '.', "“", "”"])
    fin = fin_list[:]

    # 모델 적용 후 DB에 저장
    # pred(fin)


    # me = UserTb.objects.get(user_id='test')

    # book = BookTb.objects.get(book_id = -1)


    # cnt = 0
    # for i in range(len(fin)) :
    #     print("fin[i]------------>",fin[i], fin[i][-2])
    #     if fin[i][-2].isdigit() :
    #         cnt += 1
    #         cont = ContentTb(
    #             content_id = cnt,
    #             sentence_id = cnt,
    #             text = fin[i][:-3],
    #             feelring = fin[i][-2],
    #             book = book
    #
    #         )
    #         cont.save()
    #         print("cont------------>",cont)




    return redirect('index')


# 음성서비스 페이지
def read(request):
    return render(request, 'page2.html')