from django.shortcuts import render_to_response, HttpResponse, redirect
from django.http import HttpResponseRedirect, response
from apps.freshman.models import Freshman
import json
from django.shortcuts import render
from django.views.generic.base import View
#from django.contrib.auth import login, authenticate, logout

from .forms import Applyfrom
from .models import Interview

# Create your views here.

#注册
class RegisterView(View):

    def get(self, request):
        return render(request, 'inter_register.html')

    # 面试官注册
    def post(self, request):
        try:
            applicant = Interview()
            applicant.interview_id = request.POST.get('student_id', '')  # 学号
            applicant.interview_name = request.POST.get('name', '')  # 姓名
            applicant.interview_password = request.POST.get('password', '')
            #1为开发，2为设计，3为秘书处
            applicant.interview_direction = request.POST.get('direction', '')  # 选择方向
            try:
                applicant.reason = request.POST.get('reason', '')
            except:
                applicant.reason = None

            applicant.save()
            return HttpResponse("200")  # 提交信息成功后跳转面试界面
        except:
            return HttpResponse("202")

#登录
class LoginView(View):

    def get(self, request):
        return render(request, 'inter_login.html')

    def post(self, request):
        interview_id = request.POST.get("student_id")
        interview_password = request.POST.get("password")
        check = interviewer_search(interview_id, interview_password)  # 验证:返回验证对象,失败则是None
        print(check)
        if check == '1':
            return HttpResponse("200")
        elif check == '2':
            error = "姓名错误"
            return render(request, "inter_search.html", {'error': error})
        elif check == '3':
            error = "学号错误"
            return render(request, "inter_search.html", {'error': error})
        return HttpResponse("qunimade")


#申请书
class Audition(View):
    def get(self, request):
        return render(request, 'inter_search.html')

    def post(self, request):
        return render(request, 'inter_search.html')

 # 登出
def acc_logout(request):
    # 用户登出，即删除记录登录信息的cookie
    return response('')

def interviewer_search(interview_id, interview_password):
    try:
        data = Interview.objects.get(interview_id=interview_id)
        id = data.interview_id
        password = data.interview_password
    except:
        return id #'没有注册'
    # 查有此人
    if interview_password == password:
        return '1'
    # 密码不正确
    elif interview_password != password:
        return '2'
    # 学号不正确
    elif interview_id != id:
        return '3'


# 评分和评价
def scoree_valuate(request):
    newstudent_id = request.POST.get('newstudent_id')
    score = request.POST.get('score', 0)
    interview_id = request.POST.get('interview_id', '未知')
    evaluate = request.POST.get('evaluate', '无')

    fresh = Freshman.objects.filter(newstudent_id=newstudent_id)
    fresh.score = score
    fresh.interview_id = interview_id
    fresh.evaluate = evaluate

    fresh.save()

    return render({'data' : '修改成功'})#'修改成功'

def freshman_search(request):
    # 用于模糊搜索新生,可以通过名字或者学号查
    student_id = request.POST.get('student_id', '*')
    if(student_id == ''):
        id_or_name = '*'
    else:
        id_or_name = student_id
    #之后再改，分辨是学号还是姓名
    if(id_or_name == student_id):
        data_list = Freshman.objects.filter(newname__contains=id_or_name)
        return HttpResponse(data_list)

    else:
        direction = request.POST.get('direction', '*')
        place = request.POST.get('place', '*')
        day = request.POST.get('day', '*')
        time = request.POST.get('time', '*')
        inter_type = request.POST.get('inter_type', '*')
        inter_time = day+time
        data_list = Freshman.objects.filter(direction=direction, interview_place=place, interview_time=inter_time,
                                            interview_result=inter_type)
        return HttpResponse(data_list)

# 查看新生申请书
def check_application(request):
    newstudent_id = request.POST.get('newstudent_id')
    application = ''
    try:
        application = Freshman.objects.filter(newstudent_id=newstudent_id)
    except:
        pass

    return render({'application' : application})

#内网页的登录
def internal(request):
    return render(request, 'inter_search_son.html')


def info_check_out(request):
    return None


def info_check_out_son(request):
    return None