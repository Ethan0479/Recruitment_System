from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import login
from django.contrib.auth.models import User

from .forms import Applyfrom
from .models import PersonalMessageAndInterview
# Create your views here.

# 获取学生信息那里要改，应为request.Post.get('', '')
# models中的PersonalMessageAndInterview表改为继承AbstractUser
# 实现可根据专业确定学院


# 信息填写界面
class ApplyView(View):

    def get(self, request):
        return render(request)

    def post(self, request):
        apply_form = Applyfrom(request.Post)
        if apply_form.is_valid():
            applicant = PersonalMessageAndInterview()
            applicant.student_id = request.Post.student_id   # 学号
            applicant.name = request.Post.name               # 姓名
            applicant.sex = request.Post.sex                 # 性别
            applicant.college = request.Post.college         # 学院（要实现可根据专业确定）  1.用一个dict存储专业和
            # 所属学院，填入专业后匹配学院（学院在填写信息界面不显示）
            applicant.major = request.Post.major             # 专业
            applicant.classes = request.Post.classes         # 班级（需要优化成专业班级,如：数科1803）
            applicant.phone = request.Post.phone             # 手机号
            applicant.QQ = request.Post.QQ                   # QQ
            applicant.email = request.Post.email             # 邮箱
            applicant.direction = request.Post.direction     # 选择方向
            applicant.save()
        return render(request)       # 提交信息成功后跳转面试时间预约界面/申请书提交界面


# 查询的登录界面(可查询、更改预约时间，申请书；查询面试通知，查询面试结果）（需要学号，姓名）
class SearchView(View):
    def get(self, request):
        return render(request)

    def post(self, request):
        name = request.Post.name
        student_id = request.Post.student_id
        user = User.objects.get(username=name)
        login(request, user)  # user可以是从user数据表中选出来的对象
        return render(request)  # 跳转到选择界面，选择查看预约、申请书、方向选择、面试通知或面试结果


# 方向选择查看、修改
# class DirectionView(View):
#     def get(self, request):
#         direction = PersonalMessageAndInterview.objects.get(student_id=request.user.student, name=request.user.name)
#         return render(request, )  # 显示该学生选择的方向，可修改
#
#     def post(self, request):
#         student = PersonalMessageAndInterview.objects.get(student_id=request.user.student, name=request.user.name)
#         student.direction = request.Post.direction
#         student.save()
#
#
# # 查询预约界面
# class AppointView(View):
#     def get(self, request):
#         return render(request)
#
#     def post(self, request):
#         return render(request)  # 显示该学生的预约时间，并可以修改
#
#
# # 查询申请书界面
# class ApplicationView(View):
#     def get(self, request):
#         return render(request)
#
#     def post(self, request):
#         return render(request)  # 显示该学生的申请书提交情况，并可以修改


# 面试通知界面

class ModifyView(View):
    def get(self, request):
        return render(request)

    def post(self, request):
        pass

class InterviewInformView(View):
    # 如果从查询界面得到
    def get(self, request):
        interviewed_student = PersonalMessageAndInterview.objects.get(student_id=request.user.student,
                                                                      name=request.user.name)
        interview_place = interviewed_student.interview_place
        interview_time = interviewed_student.interview_time
        application = interviewed_student.application
        if not application:
            message = '由于你未提交申请书，很抱歉你没有面试资格'
            return render(request)
        else:
            if not interview_place or not interview_time:
                message = '别着急，面试还没有开始哦'
            else:
                return render(request)
    # 如果得到此节面需要重新输入学号密码
    # def get(self, request):
    #     return render(request)
    # def post(self, request):
    #     interviewed_student = PersonalMessageAndInterview.objects.get(student_id=request.Post.student,
    #                                                                   name=request.Post.name)
    #     interview_place = interviewed_student.interview_place
    #     interview_time = interviewed_student.interview_time
    #     application = interviewed_student.application
    #     if not application:
    #         message = '由于你未提交申请书，很抱歉你没有面试资格'
    #         return render(request)
    #     else:
    #         if not interview_place or not interview_time:
    #             message = '别着急，面试还没有开始哦'
    #         else:
    #             return render(request)


# 面试结果查看界面
class InterviewResultView(View):
    def get(self, request):
        return render(request)

    def post(self, request):
        return render(request)  # 显示该学生的面试结果，不可修改

