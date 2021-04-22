from django.contrib import admin
from django.urls   import path, include
from bookApp  import  views


urlpatterns = [
# -----------------------------------------#
    # 테스트 용도
    path('test/', views.test),

    # index  / login
    path('index/', views.index, name='index'),
    path('read/', views.read, name='read'),
    path('upload/', views.upload, name='upload'),

    # signup
    path('signup/', views.signup, name='signup'),

]

