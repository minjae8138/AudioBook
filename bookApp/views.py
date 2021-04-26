from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect, get_object_or_404
from .models import *
from .forms import UserForm
from .apps import *


# # 파이썬
# import re
# import pandas as pd
# import numpy as np


# 파이썬
import re
import pandas as pd
import numpy as np
import subprocess



# 모델

# # 모델

# from konlpy.tag import Komoran
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from keras.models import load_model


# from mimetypes import guess_type



# 테스트용도
def test(request):
    users = UserTb.objects.all()
    for user in users:
        print(user.user_id)
        print(user.name)
    return render(request, 'test.html', {'posts':users})



# 모델로드 및 세팅

# # 모델로드 및 세팅

# model = load_model('nlp_model.h5')
# tokenizer = Tokenizer()
# stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
# kor = Komoran()



####################
## Page 1

# 기본페이지, 세션유지

def index(request):
    if request.session.get('user_id') and request.session.get('name'):
        # users = UserTb.objects.all()
        context = {'username':request.session['name']}
        print('logged in - ', request.session['user_id'])
        return render(request, 'page1.html', context)
    else:

        # form = LoginForm()
        # return redirect('login')
        print('login needed - ', request.session['user_id'])

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
# def pred(test_file):
#     for i in range(len(test_file)):
#         if len(test_file[i].lstrip()) == 0:
#             pass
#         else:
#             new_sentence = kor.morphs(test_file[i])
#             new_sentence = [word for word in new_sentence if not word in stopwords]
#             tokenizer.fit_on_texts(new_sentence)
#             encoded = tokenizer.texts_to_sequences([new_sentence])
#             # print(encoded)
#             pad_new = pad_sequences(encoded, maxlen=30)
#             y_pred = model.predict_classes(pad_new, verbose=1)
#             # print("before",test_file[i])
#             # test_file[i] =  del_useless(test_file[i], ['', ' ', '  ' '.', "“", "”","\r","r"])
#             test_file[i] = [test_file[i]]
#             test_file[i].append(y_pred[0])
#             # print("----------------->",test_file[i])
#             # test_file[i] = "".join(test_file[i]) + str(y_pred)
#
#     return test_file

# 모델 불러와서 감정 예측하는 함수
def get_book_evaluation_predict(text_list):
    print("start_predict")
    text_feeling_list = []
    tokenizer = BertConfig.tokenizer
    SEQ_LEN = 64
    loaded_model = BertConfig.loaded_model
    for data in text_list:
        tokens, masks, segments = [], [], []
        token = tokenizer.encode(data, max_length=SEQ_LEN, truncation=True, padding='max_length')

        num_zeros = token.count(0)
        mask = [1] * (SEQ_LEN - num_zeros) + [0] * num_zeros
        segment = [0] * SEQ_LEN

        tokens.append(token)
        segments.append(segment)
        masks.append(mask)

        tokens = np.array(tokens)
        masks = np.array(masks)
        segments = np.array(segments)
        data_x = [tokens, masks, segments]
        predict = loaded_model.predict(data_x)
        feeling = np.argmax(predict, axis=1)
        text_feeling_list.append([data, feeling[0]])

    print(text_feeling_list)
    return text_feeling_list

# tts합성을 위한 ssml태그 문자열 생성
def get_tts_woman_text(text_feeling_lists):
    book_text = "<speak>"
    pre = 9999
    b1,b2,b3,b4,b5 = 3,3,3,3,3

    for text_feeling_list in text_feeling_lists:
        text = text_feeling_list[0]
        sentiment = text_feeling_list[1]
        if sentiment == 0:
            bgm = ''
        if sentiment == 1:
            bgm = '<audio src="http://116.44.136.77/1peace.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b1),
                                                                                                        str(b1 + 3))
            b1 += 3
        if sentiment == 2:
            bgm = '<audio src="http://116.44.136.77/2angry.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b2),
                                                                                                        str(b2 + 3))
            b2 += 3
        if sentiment == 3:
            bgm = '<audio src="http://116.44.136.77/3veryangry.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b3),
                                                                                                            str(
                                                                                                                b3 + 3))
            b3 += 3
        if sentiment == 4:
            bgm = '<audio src="http://116.44.136.77/4sad.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b4),
                                                                                                      str(b4 + 3))
            b4 += 4
        if sentiment == 5:
            bgm = '<audio src="http://116.44.136.77/5janjan.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b5),
                                                                                                         str(
                                                                                                             b5 + 3))
            b5 += 5
        sentence_text = '<voice name="WOMAN_DIALOG_BRIGHT"><prosody rate="slow" volume="loud">' + bgm + text + '</prosody></voice>'
        book_text = book_text + sentence_text

    book_text = book_text + "</speak>"
    print(book_text)

    return book_text

def get_tts_man_text(text_feeling_lists):
    book_text = "<speak>"
    pre = 9999
    b1,b2,b3,b4,b5 = 3,3,3,3,3

    for text_feeling_list in text_feeling_lists:
        text = text_feeling_list[0]
        sentiment = text_feeling_list[1]
        if sentiment == 0:
            bgm = ''
        if sentiment == 1:
            bgm = '<audio src="http://116.44.136.77/1peace.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b1),
                                                                                                        str(b1 + 3))
            b1 += 3
        if sentiment == 2:
            bgm = '<audio src="http://116.44.136.77/2angry.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b2),
                                                                                                        str(b2 + 3))
            b2 += 3
        if sentiment == 3:
            bgm = '<audio src="http://116.44.136.77/3veryangry.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b3),
                                                                                                            str(
                                                                                                                b3 + 3))
            b3 += 3
        if sentiment == 4:
            bgm = '<audio src="http://116.44.136.77/4sad.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b4),
                                                                                                      str(b4 + 3))
            b4 += 4
        if sentiment == 5:
            bgm = '<audio src="http://116.44.136.77/5janjan.mp3" clipBegin="{}s" clipEnd="{}s"/>'.format(str(b5),
                                                                                                         str(
                                                                                                             b5 + 3))
            b5 += 5
        sentence_text = '<voice name="MAN_DIALOG_BRIGHT"><prosody rate="slow" volume="loud">' + bgm + text + '</prosody></voice>'
        book_text = book_text + sentence_text

    book_text = book_text + "</speak>"
    print(book_text)

    return book_text

# ssml텍스트 태그를 기반으로 음성합성 서비스
# 민재 b4e5257e61f7df0c8994a5d5eaf6ff58
# 창훈 2607c58891135f8fdd19a8d0206e9f2f
def get_tts_woman_voice(book_text):

    url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    key = "2607c58891135f8fdd19a8d0206e9f2f"
    res = subprocess.Popen(['curl', '-v', '-X', 'POST', url,
                        '-H', "Content-Type: application/xml",
                        '-H', "Authorization:"+key,
                        '-d', book_text], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    output, err = res.communicate()


    f = open('../audio/woman.wav', 'wb')

    # print(output)
    f.write(output)
    f.close()
    print(err)

def get_tts_man_voice(book_text):

    url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
    key = "2607c58891135f8fdd19a8d0206e9f2f"
    res = subprocess.Popen(['curl', '-v', '-X', 'POST', url,
                        '-H', "Content-Type: application/xml",
                        '-H', "Authorization:"+key,
                        '-d', book_text], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    output, err = res.communicate()

    f = open('../audio/man.wav', 'wb')
    # print(output)
    f.write(output)
    f.close()
    print(err)




# 파일 업로드

def upload(request) :
    file = request.FILES['text']

    # session을 통해 user_id 가져오기
    print('----------------------------> ', request.session['user_id'])
    user_id = UserTb.objects.get(user_id = request.session['user_id'])

    # book_name 가져오기
    book_name = request.POST['bookname']
    print("book_name",book_name)

    # bookTb에 파일 정보 저장
    # book = BookTb(
    #     user =  user_id,
    #     book_name = book_name
    # )
    # book.save()

    # 인코딩 작업 - 현재는 utf-8 형식의 txt파일만 업로드 가능, ansi 형식 고려x
    try :
        result_file = file.read().decode('utf-8')
        print(111)
    except:
        result_file = file.read().decode('euc-kr')
        print(222)

    # 괄호 처리
    regex_gualho = '\([^)]*\)'
    r_cont = re.sub(regex_gualho, '', result_file)

    # 개행 제거
    r_cont = re.sub("\n", " ", r_cont)
    mid = re.split('[".]', r_cont)
    fin_list = del_useless(mid, ['', ' ', '  ' '.', "“", "”"])
    fin = fin_list[:]
    # 감정예측
    text_feeling_lists = get_book_evaluation_predict(fin)
    # ssml 태그 생성
    book_text = get_tts_woman_text(text_feeling_lists)
    # ssml 태그기반 음성합성 실시
    get_tts_woman_voice(book_text)

    book_text = get_tts_man_text(text_feeling_lists)
    get_tts_man_voice(book_text)

    # print(fin)
    # 모델 적용 후 DB에 저장

    # for i in range(len(fin)) :
    #     print(i,fin[i])


    # book_id 채번
    # ---------------------------


    # 책번호 : B + '00001'
    # new_bookid= 'B' + '00001'

    # od = 1

    # 책번호
    # if od:
    #     a = od[0]['max_bookid']
    #     new_bookid = 'B' +  str(int(a[2:]) + 1).zfill(5)


    ##############
    ## contenttb에 저장 테스트 버전전
    # cont = ContentTb(
    #     # content_id= id,
    #     sentence_id = 500,
    #     text = "테스트",
    #     feelring = 3,
    #     book = book
    # )
    # cont.save()

    # content_tb에 데이터 저장
    # cnt = 0
    # for i in range(len(fin)) :
    #     print("fin[i]------------>",fin[i], fin[i][1])
    #     # if str(fin[i][1]).isdigit() :
    #     cnt += 1
    #     cont = ContentTb(
    #         sentence_id = cnt,
    #         text = fin[i][0],
    #         feelring = fin[i][1],
    #         book = book
    #
    #     )
    #     cont.save()
    #     print("cont------------>",cont)


    fin_text_list = get_book_evaluation_predict(fin)
    print(fin_text_list)

    # contentTb에 데이터 저장
    # cnt = 0
    # for i in range(len(fin)) :
    #     # print("fin[i]------------>",fin[i], fin[i][1])
    #     cnt += 1
    #     cont = ContentTb(
    #         sentence_id = cnt,
    #         text = fin_text_list[i][0],
    #         feeling = fin_text_list[i][1],
    #         book = book
    #     )
    #     cont.save()
    #     print("cont------------>",cont)

    return redirect('read')



####################
## Page 2


# 음성서비스 페이지
def read(request):



    if request.session.get('user_id') and request.session.get('name'):
        username = request.session['name']
        users = UserTb.objects.get(user_id=request.session['user_id'])
        books = BookTb.objects.all().filter(user=request.session['user_id'])

        # book_info - user_id의 여러 책중 특정 책을 가져오기 위해 리스트 형식에서 추출하기 위해 필요
        book_info = BookTb.objects.values_list().filter(user=users)
        n_len = len(book_info)
        contents = ContentTb.objects.values().filter(book = book_info[n_len-1][0])

        context = {
            'username': username,
            'users': users,
            'contents': contents,
            'books': books,
            # 'book_id': book_id,
        }
        print('logged in - ', request.session['user_id'])
        return render(request, 'page2.html', context)




# 동화책 삭제

def deleteBook(request, pk):
    bookTitle = get_object_or_404(BookTb, pk=pk)
    bookContents = ContentTb.objects.all().filter(book=pk)
    bookContents.delete()
    bookTitle.delete()
    return redirect('read')






def bookList(request) :
    if request.session.get('user_id') and request.session.get('name'):
        username = request.session['name']
        users = UserTb.objects.get(user_id=request.session['user_id'])
        books = BookTb.objects.all().filter(user=request.session['user_id'])


        bookname = request.POST.get('getBookName')

        book_info = BookTb.objects.values_list().filter(book_name=bookname)
        contents = ContentTb.objects.values().filter(book=book_info[0][0])
        print("contents------->",contents)
        context = {
            'username': username,
            'users': users,
            'contents': contents,
            'books': books,
        }
    return render(request, 'page2.html', context)







####################
## Users Related Views


# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print('success')
            return redirect('index')
        else:
            print('fail')
            return render(request, "signup.html", {'form':form})

    else:
        form = UserForm(None)
        return render(request, 'signup.html', {'form':form})



# 로그인
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth import login, authenticate


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user_id = request.POST['user_id']
        pw = request.POST['pw']
        user = UserTb.objects.get(user_id = user_id, pw = pw)
        print('user - ', user)

        context={}
        if user is not None:
            request.session['user_id'] = user.user_id
            request.session['name'] = user.name
            context['user_id'] = request.session['user_id']
            context['name'] = request.session['name']
            print('로그인 성공')
            print('user name - ', context['name'])
            return redirect('index')

        else:
            print('로그인 실패')
            return redirect('login')

            # return HttpResponse('로그인 실패')
        #
        # else:
        #     res_data = {}
        #     if not (user_id and pw):
        #         res_data['error'] = '모든 값을 입력해주세요.'
        #         print(res_data['error'])
        #
        #     else:
        #         user_id = UserTb.objects.get(user_id = user_id)
        #
        #         if check_password(pw, user_id.pw):
        #             pass
        #         else:
        #             res_data['error'] = '비밀번호가 일치하지 않습니다.'
        #             print(res_data['error'])
        #
        #     return render(request, 'login.html', res_data)

    else:
        form = LoginForm(None)
        return render(request, 'login.html', {'form':form})


# 로그아웃
def logout(request):
    request.session['user_id'] = {}
    request.session['pw'] = {}
    request.session.modified = True
    print('user_id - ', request.session['user_id'])
    print('로그아웃 성공')

    return redirect('index')

