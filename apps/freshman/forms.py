from django import forms
import re
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from .models import Freshman


class Applyfrom(forms.Form):
    newstudent_id = forms.CharField(required=True)
    password = forms.CharField(required=True)
    newname = forms.CharField(required=True)
    gender = forms.CharField(required=True)
    # college = forms.ModelChoiceField((('学院1', 1), ('学院2', 2), ('学院3', 3)), required=True)
    college = forms.CharField(required=True)  # 下拉框
    major = forms.CharField(required=True)  # 下拉框
    newclass = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    qq = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    apartment = forms.CharField(required=True)
    dormitory = forms.CharField(required=True)

    def clean_newstudent_id(self):
        newstudent_id = self.cleaned_data.get('newstudent_id')
        regex = re.compile('^2019\\d{6}$')
        if regex.match(newstudent_id):
            if Freshman.objects.filter(newstudent_id=newstudent_id):
                raise forms.ValidationError('你已经报名啦，不需要重复报名', code='duplicated application')
            else:
                return newstudent_id
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
    def clean_newname(self):
        newname = self.cleaned_data.get('newname')
        processed_name = re.sub('·', '', newname)
        regex = re.compile('[\u4E00-\u9FA5]{2,10}')
        if regex.match(processed_name):
            return newname
        else:
            raise forms.ValidationError('名字格式不正确', code='wrong name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Freshman.objects.filter(email=email):
            raise forms.ValidationError('该邮箱已注册', code='duplicated email')
        else:
            return email


class ModifyForm(forms.Form):
    password = forms.CharField(required=True)
    college = forms.CharField(required=True)  # 下拉框
    major = forms.CharField(required=True)  # 下拉框
    newclass = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    qq = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        regex = re.compile('^1((3[0-9])|(4[579])|(5[469])|(66)|(7[35678])|(8[0-9])|(9[89]))\\d{8}$')
        if regex.match(phone):
            return phone
        else:
            raise forms.ValidationError('手机号格式不正确', code='wrong phone')
