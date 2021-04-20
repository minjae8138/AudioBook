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