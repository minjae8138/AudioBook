from django.contrib import admin
from django.urls   import path, include
from bookApp  import  views


urlpatterns = [
# -----------------------------------------#
    # 테스트 용도
    path('test/', views.test),

    # Page 1(index) / login redirect
    path('index/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),

    # users
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # Page 2
    path('read/', views.read, name='read'),
    path('<pk>/delete/', views.deleteBook, name='delete'),
    path('bookList/', views.bookList, name='bookList'),

]

