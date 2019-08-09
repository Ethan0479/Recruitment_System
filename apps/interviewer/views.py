from django.shortcuts import render_to_response, HttpResponse, redirect
from django.http import HttpResponseRedirect, response
from apps.freshman.models import Freshman
import json
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import login, authenticate, logout

from .forms import Applyfrom
from .models import Interview


# Create your views here.


def interviewer_search(request):
    # 用于查找面试官
    cookie = request.COOKIES.get("user_info", None)
    if cookie:
        cookie = cookie.replace('\'', '\"')
        user_info = json.loads(cookie, strict=False)

        interview_id = user_info.get('interview_id')
        interview_name = user_info.get('interview_name')

        id = Interview.objects.filter(interview_id=interview_id)
        name = Interview.objects.filter(interview_name=interview_name)

        if interview_name == name and interview_id == id:
            return interview_id, interview_name
        else:
            return '没有注册'
    else:
        return None, None


def freshman_search(request):
    # 用于模糊搜索新生,可以通过名字或者学号查
    cookie = request.COOKIES.get("user_info", None)
    if cookie:
        cookie = cookie.replace('\'', '\"')
        user_info = json.loads(cookie, strict=False)

        info = user_info.get('info')

        name_list = Freshman.objects.filter(newname__contains=info)
        id_list = Freshman.objects.filter(newstudent_id__contains=info)

        return name_list, id_list
    else:
        return None


class Applyfrom(View):

    def get(self, request):
        return render(request)

    # 面试官注册
    def post(self, request):
        apply_form = Applyfrom(request.Post)
        if apply_form.is_valid():
            applicant = Interview()
            applicant.interview_id = request.Post.get('id', '')  # 学号
            applicant.interview_name = request.Post.get('name', '')  # 姓名
            applicant.interview_direction = request.Post.get('direction', '')  # 选择方向
            try:
                applicant.reason = request.Post.get('reason', '')
            except:
                applicant.reason = None

            applicant.save()
        return render(request)  # 提交信息成功后跳转面试界面


class SearchView(View):

    # 登录
    def acc_login(self, request):
        if request.method == "GET":
            return render(request, ".html")
        else:
            interview_id = request.POST.get("id")
            interview_name = request.POST.get("name")
            user = authenticate(interview_id=interview_id, interview_name=interview_name)  # 验证:返回验证对象,失败则是None
            if user:
                login(request, user)
                return redirect('.html')
            else:
                error = "学号或姓名错误"
                return render(request, ".html", {'error': error})

    # 登出
    def acc_logout(self, request):
        # 用户登出，即删除记录登录信息的cookie
        logout(request)
        return response('')


class Audition(View):

    # 查看新生申请书
    def check_application(self, request):
        newstudent_id = request.POST.get('newstudent_id')
        application = ''
        try:
            application = Freshman.objects.filter(newstudent_id=newstudent_id)
        except:
            pass

        return application

    # 评分和评价
    def scoree_valuate(self, request):
        newstudent_id = request.POST.get('newstudent_id')
        score = request.POST.get('score', 0)
        interview_id = request.POST.get('interview_id', '未知')
        evaluate = request.POST.get('evaluate', '无')

        fresh = Freshman.objects.filter(newstudent_id=newstudent_id)
        fresh.score = score
        fresh.interview_id = interview_id
        fresh.evaluate = evaluate

        fresh.save()

        return '修改成功'
