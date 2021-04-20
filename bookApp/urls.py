from django.contrib import admin
from django.urls   import path, include
from bookApp  import  views

##
from django.conf import settings
from django.conf.urls.static import static
##

urlpatterns = [
# -----------------------------------------#
    # index  / login
    path('index/', views.index, name='index'),
    path('read/', views.read, name='read'),
    # path('upload/', views.upload, name='upload'),

]

##
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
##