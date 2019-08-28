from django.shortcuts import render_to_response, HttpResponse
from django.http import response, HttpResponseRedirect
from apps.freshman.models import Freshman
import re
import json
from django.shortcuts import render, redirect
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
        check = interviewer_search(interview_id, interview_password)
        if check == '登录成功':
            student = Interview.objects.get(interview_id=interview_id)
            interview_name = student.interview_name
            request.session['interview_id'] = interview_id
            request.session['interview_name'] = interview_name
            return redirect('../management')
        elif check == '密码不正确':
            error = "密码错误"
            return HttpResponse(error)
        elif check == '学号不存在，请先注册':
            error = "学号不存在，请先注册"
            return HttpResponse(error)
        return HttpResponse("错误")

def interviewer_search(interview_id, interview_password):
    try:
        data = Interview.objects.get(interview_id=interview_id)
        password = data.interview_password
    except:
        return '学号不存在，请先注册'  # '学号不存在'
    # 查有此人
    if interview_password == password:
        return '登录成功'
    # 密码不正确
    elif interview_password != password:
        return '密码不正确'

# 申请书
class Audition(View):
    def get(self, request):
        try:
            interview_id = request.session.get('interview_id')
            interview_name = request.session.get('interview_name')
            if interview_id and interview_name:
                number = Freshman.objects.all()
                number = len(number)
                return render(request, 'inter_search.html', {'number': number})
            else:
                return HttpResponseRedirect("../login/")
        except:
            return HttpResponseRedirect("../login/")

    def post(self, request):
        try:
            interview_id = request.session.get('interview_id')
            interview_name = request.session.get('interview_name')
            if interview_id and interview_name:
                number = Freshman.objects.all()
                number = len(number)
                return render(request, 'inter_search.html', {'number': number})
            else:
                return HttpResponseRedirect("../login/")
        except:
            return HttpResponseRedirect("../login/")

# 登出
def acc_logout(request):
    # 用户登出，即删除记录登录信息的cookie
    return response('')

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
#过滤筛选
def freshman_search(request):
    id_or_name = request.POST.get("student_id", "")
    direction = request.POST.get("direction", "")
    place = request.POST.get("place", "")
    time = request.POST.get("time", "")
    inter_type = request.POST.get("inter_type", "")

    all_student_data = Freshman.objects.all()

    if id_or_name == '':
        pass
    else:
        regex = re.compile(r'^2019+\d{0,6}')
        if regex.match(id_or_name):
            data_list = Freshman.objects.filter(newstudent_id__contains=id_or_name)
            return render_to_response('inter_search_son.html', {"data_list": (data_list), "number": len(all_student_data),
                                                         "num": len(data_list)})
        else:
            data_list = Freshman.objects.filter(newname__contains=id_or_name)
            return render_to_response('inter_search_son.html', {"data_list": (data_list), "number": len(all_student_data),
                                                         "num": len(data_list)})

    if direction != '':
        all_student_data = Freshman.objects.filter(direction=direction)
    if place != '':
        all_student_data = all_student_data.filter(place=place)
    if time != '':
        all_student_data = all_student_data.filter(interview_time=time)
    if inter_type != '':
        all_student_data = all_student_data.filter(interview_result=inter_type)

    data_list = []
    for people in all_student_data:
        data_list.append({"newstudent_id": people.newstudent_id, "newname": people.newname, "gender": people.gender,
                         "college": people.college, "major": people.major, "time": people.interview_time,
                         "interview_place": people.interview_place,
                         "direction": people.direction, "evaluate": people.evaluate})

    return render_to_response('inter_search_son.html', {"data_list": (data_list), "number": len(all_student_data),
                                                        "num":len(data_list)})
#查看自己面试过的人
def interviewed(request):
    interview_id = request.session.get('interview_id')
    interviewed_student = Freshman.objects.filter(interview_id=interview_id)
    data_list = []
    for people in interviewed_student:
        data_list.append({"newstudent_id": people.newstudent_id, "newname": people.newname, "gender": people.gender,
                          "college": people.college, "major": people.major, "time": people.interview_time,
                          "interview_place": people.interview_place,
                          "direction": people.direction, "evaluate": people.evaluate})
    return render_to_response('inter_search_son.html', {"data_list": (data_list), "num":len(data_list)})

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

