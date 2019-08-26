# _*_ encoding:utf-8 _*_
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class GlobalSettings(object):
    site_title = '后台管理系统'
    site_footer = '云顶书院'


class Freshman(models.Model):

    # 学号， 姓名， 性别， 学院， 专业， 专业班级， 手机号， QQ， 邮箱为必填， 申请时填入

    newstudent_id = models.CharField(max_length=11, verbose_name=u'学号')#username存储学号
    password = models.CharField(max_length=25, verbose_name='密码')
    newname = models.CharField(max_length=50, verbose_name=u'姓名')
    gender = models.CharField(max_length=5, verbose_name='性别')
    college = models.CharField(max_length=30, verbose_name='所属学院')
    major = models.CharField(max_length=100, verbose_name='所属专业')
    newclass = models.CharField(max_length=20, verbose_name='班级')
    phone = models.CharField(max_length=11, verbose_name='手机')
    qq = models.CharField(max_length=15, verbose_name='QQ号')
    email = models.EmailField(max_length=30, verbose_name='邮箱')

    # 预约时间， 申请书， 面试时间， 面试地点， 面试得分， 评价， 面试者， 面试结果为后续填入事项，设为不必填
    direction = models.CharField(max_length=15, verbose_name='选择方向', choices=(('development', '开发'), ('design', '设计'), ('secretariat', '秘书处')), null=True, blank=True)
    appointment_one = models.CharField(verbose_name='预约时间一', null=True, blank=True, max_length=60)
    appointment_two = models.CharField(verbose_name='预约时间二', null=True, blank=True, max_length=60)
    appointment_three = models.CharField(verbose_name='预约时间三', null=True, blank=True, max_length=60)
    application = RichTextField(null=True, blank=True, verbose_name='申请书')
    interview_time = models.CharField(verbose_name='面试时间', null=True, blank=True, max_length=60)
    interview_place = models.CharField(max_length=50, verbose_name='面试地点', blank=True, null=True)
    score = models.IntegerField(verbose_name='评分', null=True, blank=True)
    evaluate = models.TextField(max_length=300, verbose_name='评价', null=True, blank=True)
    interview_result_A = models.BooleanField(verbose_name='A轮面试结果', null=True, blank=True)
    interview_result_B = models.BooleanField(verbose_name='B轮面试结果', null=True, blank=True)
    interview_name = models.CharField(max_length=60, verbose_name='面试官', null=True, blank=True)
    province = models.CharField(max_length=30, verbose_name='省份', null=True, blank=True)
    apartment = models.CharField(max_length=25, verbose_name='宿舍楼', null=True, blank=True)
    dormitory = models.CharField(max_length=25, verbose_name='宿舍号', null=True, blank=True)
    remark_1 = models.CharField(max_length=255, verbose_name='备注1', null=True, blank=True)
    remark_2 = models.CharField(max_length=255, verbose_name='备注2', null=True, blank=True)
    remark_3 = models.CharField(max_length=255, verbose_name='备注3', null=True, blank=True)
    class Meta:
        verbose_name = u'新生信息'
        verbose_name_plural = u'新生信息'

    def __str__(self):
        return self.newname

class Academy(models.Model):
    academy = models.CharField(max_length=30, verbose_name='学院')

    class Meta:
        verbose_name = u'学院信息'
        verbose_name_plural = u'学院信息'

    def __str__(self):
        return self.academy

class Major(models.Model):
    major = models.CharField(max_length=30,verbose_name='专业')
    majorAcademy = models.ForeignKey(Academy, on_delete=models.CASCADE,verbose_name='所属学院')

    class Meta:
        verbose_name = u'专业信息'
        verbose_name_plural = u'专业信息'

    def __str__(self):
        return self.major
