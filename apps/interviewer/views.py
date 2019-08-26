from django.shortcuts import render_to_response, HttpResponse
from django.http import response
from apps.freshman.models import Freshman
import re
from django.shortcuts import render
from django.views.generic.base import View
# from django.contrib.auth import login, authenticate, logout

from .forms import Applyfrom
from .models import Interview


# Create your views here.

# 注册
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
            # 1为开发，2为设计，3为秘书处
            applicant.interview_direction = request.POST.get('direction', '')  # 选择方向
            try:
                applicant.reason = request.POST.get('reason', '')
            except:
                applicant.reason = None

            applicant.save()
            return HttpResponse("200")  # 提交信息成功后跳转面试界面
        except:
            return HttpResponse("202")


# 登录
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


# 申请书
class Audition(View):
    def get(self, request):
        number = Freshman.objects.all()
        number = len(number)
        return render(request, 'inter_search.html', {'number': number})

    def post(self, request):
        number = Freshman.objects.all()
        number = len(number)
        return render(request, 'inter_search.html', {'number': number})


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
        return id  # '没有注册'
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

    return render({'data': '修改成功'})  # '修改成功'

def freshman_search(request):
    id_or_name = request.POST.get("student_id", "")
    direction = request.POST.get("direction", "")
    place = request.POST.get("place", "")
    time = request.POST.get("time", "")
    inter_type = request.POST.get("inter_type", "")

    if id_or_name == '':
        pass
    else:
        regex = re.compile('^2019\\*{0,6}')
        if regex.match(id_or_name):
            student_data = Freshman.objects.filter(newstudent_id__contains=id_or_name)
            return student_data
        else:
            student_data = Freshman.objects.filter(newname__contains=id_or_name)
            return student_data

    all_student_data = Freshman.objects.all()
    if direction != '':
        all_student_data = Freshman.objects.filter(direction=direction)
    if place != '':
        all_student_data = all_student_data.filter(place=place)
    if time != '':
        all_student_data = all_student_data.filter(time=time)
    if inter_type != '':
        all_student_data = all_student_data.filter(inter_type=inter_type)

    data_list = []
    for people in all_student_data:
        data_list.append({"newstudent_id": people.newstudent_id, "newname": people.newname, "gender": people.gender,
                         "college": people.college, "major": people.major, "time": time,
                         "interview_place": people.interview_place,
                         "direction": people.direction, "evaluate": people.evaluate})
    return render_to_response('inter_search_son.html', {"data_list": (data_list), "number": len(data_list)})

def info_check_out(request,a):
    if request.method == 'GET':
        stu = Freshman.objects.get(newstudent_id=a)
        return render(request, 'student_info.html', {'a': stu})
    else:
        question = request.POST.get("question",'')
        evaluate = request.POST.get('evaluate','')
        if question == '':
            pass
        if evaluate == '':
            pass
        return HttpResponse(200)

def info_check_out_son(request,a):
    print(a)
    return HttpResponse(200)

