from django.contrib import admin


# admin.site.register(index)
from bookApp.models import BookTb, ContentTb, UserTb


# Register your models here.
admin.site.register(BookTb)
admin.site.register(ContentTb)
admin.site.register(UserTb)
