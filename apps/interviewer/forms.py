from django import forms
import re
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from .models import Interview


class Applyfrom(forms.Form):
    interview_id = forms.CharField(required=True),
    interview_name = forms.CharField(required=True),
    interview_direction = forms.CharField(required=True)

    def clean_interview_id(self):
        interview_id = self.cleaned_data.get('interview_id')
        regex = re.compile('^2019\\d{6}$')
        if regex.match(interview_id):
            if Interview.objects.filter(interview_id=interview_id):
                raise forms.ValidationError('你已经报名啦，不需要重复报名', code='duplicated application')
            else:
                return interview_id
        else:
            raise forms.ValidationError('学号格式不正确', code='wrong student_id')


    #检验名字全为汉字
    def clean_name(self):
        name = self.cleaned_data.get('name')
        processed_name = re.sub('·', '', name)
        regex = re.compile('[\u4E00-\u9FA5]{2,10}')#名字中有·的怎么解决
        if regex.match(processed_name):
            return name
        else:
            raise forms.ValidationError('名字格式不正确', code='wrong name')

