from django import forms
from django.contrib.auth.hashers import check_password
from django.forms import Form

# from .models import UploadFileModel

# class UploadFileForm(forms.Form):
#     class Meta:
#         model = UploadFileModel
#         fields = ('title', 'file')

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False


class DocumentForm(forms.Form):
    docfile  = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


# 회원가입 폼

from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

# 회원가입 폼
class UserForm(forms.ModelForm):

    class Meta:
        model = UserTb
        fields = ['user_id', 'pw', 'name', 'e_mail']
        widgets = {
            'pw' : forms.PasswordInput(),
            'e_mail' : forms.EmailInput(),
        }



# 로그인 폼

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserTb
        fields = ['user_id', 'pw']
        widgets = {
            'user_id' : forms.TextInput(
                attrs={'autocomplete': 'off'},
            ),
            'pw' : forms.PasswordInput(),
        }
