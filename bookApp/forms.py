from django import forms
from django.forms import Form

from .models import UploadFileModel

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

class UserForm(forms.ModelForm):
    class Meta:
        model = UserTb
        fields = ['user_id', 'pw', 'name', 'e_mail']

    # 유효성 체크
    def clean(self):

        super(UserForm, self).clean()

        pw = self.cleaned_data.get('pw')
        name = self.cleaned_data.get('name')

        # 임의로 조건 설정했습니다
        if len(pw) < 9 :
            self._errors['password'] = self.error_class([
                '최소 8자 이상 입력해주세요.'])
        if len(name) < 4 :
            self._errors['nickname'] = self.error_class([
                '최소 3자 이상 입력해주세요.'
            ])

        return self.cleaned_data