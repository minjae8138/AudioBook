from django.contrib import admin
from django.urls   import path, include
from bookApp  import  views



urlpatterns = [
# -----------------------------------------#
    # index  / login
    path('index/', views.index, name='index'),
    path('read/', views.read, name='read'),

]


