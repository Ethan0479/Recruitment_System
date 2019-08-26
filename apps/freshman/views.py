from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

import random
import time
import json

from .forms import Applyfrom, ModifyForm
from .models import Freshman, Academy, Major
from Recruitment_System.settings import EMAIL_FROM


# Create your views here.

# 获取学生信息那里要改，应为request.Post.get('', '')
# 实现可根据专业确定学院
'''
登陆
注册
个人信息修改
提交申请书
面试时间（修改/确定）
面试（时间/地点/结果）查询
'''


# def page_not_found(request, exception, template_name='new_404.html'):
#     return render(request, template_name)
#
#
# def server_error(request, template_name='new_500.html'):
#     return render(request, template_name)


class IndexView(View):
    def get(self, request):
        return render(request, '../freshman_templates/index.html')


# 注册、信息填写界面
class RegisterView(View):

    def get(self, request):
        apply_form = Applyfrom()
        colleges = Academy.objects.all()
        return render(request, '../freshman_templates/register.html', {'colleges': colleges})

    def post(self, request):
        apply_form = Applyfrom(request.POST)
        if apply_form.is_valid():
            applicant = Freshman()
            applicant.newstudent_id = request.POST.get('newstudent_id', '')  # 学号
            applicant.password = request.POST.get('password', '')  # 密码
            applicant.newname = request.POST.get('newname', '')  # 姓名
            applicant.gender = request.POST.get('gender', '')  # 性别
            applicant.college = request.POST.get('college', '')  # 学院（要实现可根据专业确定）  1.用一个dict存储专业和
            # 所属学院，填入专业后匹配学院（学院在填写信息界面不显示）
            applicant.major = request.POST.get('major', '')  # 专业
            applicant.newclass = request.POST.get('newclass', '')  # 班级（需要优化成专业班级,如：数科1803）
            applicant.phone = request.POST.get('phone', '')  # 手机号
            applicant.qq = request.POST.get('qq', '')  # QQ
            applicant.email = request.POST.get('email', '')  # 邮箱
            applicant.apartment = request.POST.get('apartment', '')
            applicant.dormitory = request.POST.get('dormitory', '')

            applicant.save()
            # response = redirect('/login/')
            return HttpResponse("200")  # 注册成功跳转登录页面
            # else:
            #     return render(request, 'register.html', {'error': error})
        else:
            errors = []
            for error in apply_form.errors:
                errors.append(error)
            error_list = ','.join(errors)
            return HttpResponse(error_list)
            # return render(request, '../freshman_templates/register.html')  # 提示错误信息

# 随机生成数字验证码
def generate_code():
    num_list = []
    for i in range(6):
        num_list.append(str(random.randint(0, 9)))
    num_code = ''.join(num_list)
    return num_code


# 可能需要重写
def send_code_by_email(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        title = '注册验证码'
        code = generate_code()
        content = '验证码为：' + code
        status = send_mail(title, content, EMAIL_FROM, [email])
        return HttpResponse(status)


def get_major(request):
    if request.method == 'POST':
        college = request.POST.get('academy', '')
        if not college:
            return HttpResponse('')
        else:
            college_id = Academy.objects.get(academy=college).id
            majors = Major.objects.filter(majorAcademy_id=college_id)
            majors_name = []
            for i in range(len(majors)):
                majors_name.append(majors[i].major)
            majors_str = ','.join(majors_name)
            return HttpResponse(majors_str)


# 查询的登录界面(可查询、更改预约时间，申请书；查询面试通知，查询面试结果）（需要学号，密码）
class LoginView(View):
    def get(self, request):
        return render(request, '../freshman_templates/login.html')

    def post(self, request):
        newstudent_id = request.POST.get('newstudent_id', '')
        password = request.POST.get('password', '')
        # user = authenticate(username=student_id, password=password)
        try:
            user = Freshman.objects.get(newstudent_id=newstudent_id)
            if password == '':
                json_error = json.dumps({'error': '表乱来，密码还没填呢'})
                return render(request, '../freshman_templates/login.html',{'error': json_error, 'student_id': user.newstudent_id})
            else:
                if user is not None:
                    if user.password == password:
                        # url = '/index/' + newstudent_id + '/'
                        url = '/homepage/'
                        response = redirect(url)
                        response.set_cookie('newstudent_id', newstudent_id)
                        response.set_cookie('idnum', user.id)
                        return response  # 跳转到选择界面，选择查看预约、申请书、方向选择、面试通知或面试结果
                    else:
                        json_error = json.dumps({'error': '啊，用户名和密码不匹配呀！'})
                        return render(request, '../freshman_templates/login.html', {'error': json_error, 'student_id': user.newstudent_id})
        except Freshman.DoesNotExist:
            json_data = json.dumps({'error': '同学还没有注册吧，先注册哦'})
            return render(request, '../freshman_templates/login.html', {'error': json_data})


def student_search(request):
    newstudent_id = request.COOKIES.get('newstudent_id', '')
    if newstudent_id == '' or not newstudent_id:
        return 'no_student_id'
    else:
        return newstudent_id


class HomepageView(View):
    def get(self, request):
        newstudent_id = student_search(request)
        if newstudent_id == 'no_student_id':
            return redirect('/login/')
        else:
            student = Freshman.objects.get(newstudent_id=newstudent_id)
            return render(request, '../freshman_templates/homepage.html', {'student': student})


# 个人信息查看、修改(姓名、学号、性别不可改，方向不在此处修改)
# 改进：需设置登录后才能访问
class PersonalView(View):
    def get(self, request):
        newstudent_id = student_search(request)
        if newstudent_id == 'no_student_id':
            return redirect('/login/')
        else:
            student = Freshman.objects.get(newstudent_id=newstudent_id)  # 根据cookie中的newstudent_id在数据库中取出该学生传给前端
            colleges = Academy.objects.all()
            return render(request, '../freshman_templates/alterinfo.html', {'student': student, 'colleges': colleges})

    def post(self, request):
        newstudent_id = request.COOKIES.get('newstudent_id', '')
        student = Freshman.objects.get(newstudent_id=newstudent_id)
        modify_form = ModifyForm(request.POST)  # 验证手机号的格式是否正确
        if modify_form.is_valid():
            same_phones = Freshman.objects.filter(phone=request.POST.get('phone', ''))
            same_emails = Freshman.objects.filter(email=request.POST.get('email',''))
            dumplicated_phone = None
            dumplicated_email = None
            # 根据id检验手机号是否与别人重复
            for same_phone in same_phones:
                if same_phone.id != student.id:
                    dumplicated_phone = '新手机号已经被用过啦！'
                    break
            for same_email in same_emails:
                if same_email.id != student.id:
                    dumplicated_email = '新邮箱已经被用过啦！'
                    break
            # 如果不重复则保存，有重复则返回该页面并提示
            if not dumplicated_phone and not dumplicated_email:
                student.password = request.POST.get('password', '')
                student.college = request.POST.get('college', '')
                student.major = request.POST.get('major', '')
                student.newclass = request.POST.get('newclass', '')
                student.phone = request.POST.get('phone', '')  # 手机号
                student.qq = request.POST.get('qq', '')  # QQ
                student.email = request.POST.get('email', '')  # 邮箱
                student.apartment = request.POST.get('apartment', '')  # 宿舍楼
                student.dormitory = request.POST.get('dormitory', '')  # 宿舍号
                student.save()
                return HttpResponse("200")  # 成功则返回主页面
                # if newstudent_id == student.newstudent_id:  # 没改学号正常跳回index页面
                #     return render(request, 'index.html', {'msg': msg})
                # else:  # 改了学号则需要退出并重新登录
                #     response = log_out(request)
                #     return response
            elif not dumplicated_email:
                return HttpResponse(dumplicated_phone)
            elif not dumplicated_phone:
                return HttpResponse(dumplicated_email)
            else:
                return HttpResponse("202")
        else:
            errors = []
            for error in modify_form.errors:
                errors.append(error)
            error_list = ','.join(errors)
            return HttpResponse(error_list)  # 提示错误信息


# 选择、修改预约时间和方向（报名）界面
class AppointmentView(View):
    def get(self, request):
        newstudent_id = student_search(request)
        if newstudent_id == 'no_student_id':
            return redirect('/login/')
        else:
            student = Freshman.objects.get(newstudent_id=newstudent_id)
            if not student.direction and not student.appointment_one:
                return render(request, '../freshman_templates/sign_up.html', locals())  # 没选择方向以及至少一个预约时间的话跳转报名界面
            else:
                return render(request, '../freshman_templates/sign_up_success.html', {'student': student})  # 选择了跳转报名成功界面

    def post(self, request):
        student = Freshman.objects.get(newstudent_id=request.COOKIES.get('newstudent_id', ''))
        student.appointment_one = request.POST.get('appointment_one', '')
        student.appointment_two = request.POST.get('appointment_two', '')
        student.appointment_three = request.POST.get('appointment_three', '')
        student.direction = request.POST.get('direction', '')
        student.save()
        msg = '选择成功！记得关注面试通知哦！'
        return HttpResponse("200")  # 可以修改


# 修改报名
class AlterAppointmentView(View):
    def get(self, request):
        newstudent_id = student_search(request)
        if newstudent_id == 'no_student_id':
            return redirect('/login/')
        else:
            student = Freshman.objects.get(newstudent_id=newstudent_id)
            direction = student.direction
            time1 = student.appointment_one
            time2 = student.appointment_three
            time3 = student.appointment_two
            return render(request, '../freshman_templates/alter_sign_up.html',{'student':student})

    def post(self, request):
        student = Freshman.objects.get(newstudent_id=request.COOKIES.get('newstudent_id', ''))
        student.appointment_one = request.POST.get('appointment_one', '')
        student.appointment_two = request.POST.get('appointment_two', '')
        student.appointment_three = request.POST.get('appointment_three', '')
        student.direction = request.POST.get('direction', '')
        student.save()
        msg = '修改成功！记得关注面试通知哦！'
        return HttpResponse("200")


# 查询、修改申请书界面
class ApplicationView(View):
    def get(self, request):  # 显示该学生的申请书提交情况
        newstudent_id = student_search(request)
        if newstudent_id == 'no_student_id':
            return redirect('/login/')
        else:
            student = Freshman.objects.get(newstudent_id=newstudent_id)
            tip = ''
            if not student.application:
                tip = '记得及时提交申请书哦，不然就没有面试资格啦！'
            return render(request, '../freshman_templates/editor.html', {'student': student, 'tip': tip})

    def post(self, request):  # 可以修改
        student = Freshman.objects.get(newstudent_id=request.COOKIES.get('newstudent_id', ''))
        student.application = request.POST.get('content', '')
        student.save()
        time.sleep(2)
        return redirect('/homepage/')


# 面试通知界面
# class InterviewInformView(View):
#     # 如果从查询界面得到
#     def get(self, request):
#         interviewed_student = Freshman.objects.get(student_id=request.user.student,
#                                                    name=request.user.name)
#         interview_place = interviewed_student.interview_place
#         interview_time = interviewed_student.interview_time
#         application = interviewed_student.application
#         if not application:
#             message = '由于你未提交申请书，很抱歉你没有面试资格'
#             return render(request)
#         else:
#             if not interview_place or not interview_time:
#                 message = '别着急，面试还没有开始哦'
#             else:
#                 return render(request)


# 面试结果查看界面
class InterviewResultView(View):
    def get(self, request):  # 显示该学生的面试结果，不可修改
        newstudent_id = student_search(request)
        if newstudent_id == 'no_student_id':
            return redirect('/login/')
        else:
            student = Freshman.objects.get(newstudent_id=newstudent_id)
            # 大概逻辑
            if not student.interview_result:
                return
            else:
                if '通过' in student.interview_result:  # 面试成功
                    return render(request, '../freshman_templates/succ_inter.html', {'student': student})
                else:                                    # 面试失败
                    return render(request, '../freshman_templates/faul_inter.html', {'student': student})


# 退出函数
def log_out(request):
    response = render(request, '../freshman_templates/login.html')
    response.delete_cookie('newstudent_id')
    response.delete_cookie('idnum')
    return response


def page_not_found(request):
    """
    全局 404 处理函数
    """
    from django.shortcuts import render_to_response
    response = render_to_response('404.html',{})
    response.status_code = 404
    return response