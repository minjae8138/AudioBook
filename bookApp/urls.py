from django.contrib import admin
from django.urls   import path, include
from bookApp  import  views


urlpatterns = [
# -----------------------------------------#
    # 테스트 용도
    path('test/', views.test),

    # index / login redirect
    path('index/', views.index, name='index'),
    path('read/', views.read, name='read'),
    path('upload/', views.upload, name='upload'),

    # users
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # bookList
    path('editTitle/', views.editTitle, name='editTitle'),
    path('/<int:book_id>/deleteBook/', views.deleteBook, name='deleteBook'),

]

