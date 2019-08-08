from django import forms
import re
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from .models import Freshman


class Applyfrom(forms.Form):
    student_id = forms.CharField(required=True),
    name = forms.CharField(required=True),
    sex = forms.CharField(required=True),
    college = forms.CharField(required=True),
    major = forms.CharField(required=True),
    classes = forms.CharField(required=True),
    phone = forms.CharField(required=True),
    QQ = forms.CharField(required=True),
    email = forms.CharField(required=True),
    direction = forms.CharField(required=True)

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        regex = re.compile('^2019\\d{6}$')
        if regex.match(student_id):
            if Freshman.objects.filter(student_id=student_id):
                raise forms.ValidationError('你已经报名啦，不需要重复报名', code='duplicated application')
            else:
                return student_id
        else:
            raise forms.ValidationError('学号格式不正确', code='wrong student_id')

    # def clean_classes(self):
    #     Class = self.cleaned_data.get('classes')
    #     regex = re.compile('[\u4E00-\u9FA5]{2}19\\d{2}$')#两个汉字加四个数字，数字以19开头，如：数科1903
    #     if regex.match(Class):
    #         return Class
    #     else:
    #         raise forms.ValidationError('班级格式不正确', code='wrong class')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        regex = re.compile('^1((3[0-9])|(4[579])|(5[469])|(66)|(7[35678])|(8[0-9])|(9[89]))\\d{8}$')
        if regex.match(phone):
            if Freshman.objects.filter(phone=phone):
                raise forms.ValidationError('该手机号已提交', code='duplicated phone')
            else:
                return phone
        else:
            raise forms.ValidationError('手机号格式不正确', code='wrong phone')

    #检验名字全为汉字
    def clean_name(self):
        name = self.cleaned_data.get('name')
        processed_name = re.sub('·', '', name)
        regex = re.compile('[\u4E00-\u9FA5]{2,10}')#名字中有·的怎么解决
        if regex.match(processed_name):
            return name
        else:
            raise forms.ValidationError('名字格式不正确', code='wrong name')
