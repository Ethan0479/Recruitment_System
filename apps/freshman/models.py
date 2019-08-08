# _*_ encoding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class GlobalSettings(object):
    site_title = '后台管理系统'
    site_footer = '云顶书院'


class Freshman(AbstractUser):   # 此处继承AbstractUser， 改写auth_user表，以便登录

    # 学号， 姓名， 性别， 学院， 专业， 专业班级， 手机号， QQ， 邮箱， 方向为必填， 申请时填入

    # newstudent_id = models.CharField(max_length=11, verbose_name=u'学号')#username存储学号
    newname = models.CharField(max_length=50, verbose_name=u'姓名')
    gender = models.CharField(max_length=5, verbose_name='性别')
    college = models.CharField(max_length=30, verbose_name='所属学院')
    major = models.CharField(max_length=100, verbose_name='所属专业')
    newclass = models.CharField(max_length=20, verbose_name='班级')
    phone = models.CharField(max_length=11, verbose_name='手机')
    qq = models.CharField(max_length=15, verbose_name='QQ号')
    email = models.CharField(max_length=30, verbose_name='邮箱')
    direction = models.CharField(max_length=15, verbose_name='选择方向', choices=(('development', '开发'), ('design', '设计'), ('secretariat', '秘书处')))

    # 预约时间， 申请书， 面试时间， 面试地点， 面试得分， 评价， 面试者， 面试结果为后续填入事项，设为不必填

    appointment_one = models.DateTimeField(verbose_name='预约时间一', null=True, blank=True)
    appointment_two = models.DateTimeField(verbose_name='预约时间二', null=True, blank=True)
    application = RichTextUploadingField(null=True, blank=True, verbose_name='申请书')
    interview_time = models.DateTimeField(verbose_name='面试时间', null=True, blank=True)
    interview_place = models.CharField(max_length=50, verbose_name='面试地点', blank=True, null=True)
    score = models.IntegerField(verbose_name='评分', null=True, blank=True)
    evaluate = models.TextField(max_length=300, verbose_name='评价', null=True, blank=True)
    interview_result = models.CharField(max_length=50, choices=(('A_passd', '面试A轮通过'), ('A_failed', '面试A轮失败'), ('B_passd', '面试B轮通过'), ('B_failed', '面试B轮失败')), verbose_name='面试结果', null=True, blank=True)
    interview_name = models.CharField(max_length=60, verbose_name='面试官', null=True, blank=True)

    class Meta:
        verbose_name = u'新生信息'
        verbose_name_plural = u'新生信息'

    def __str__(self):
        return self.newname
