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
        return render(request, 'interviewer_register.html')

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
        return render(request, "interviewer_register.html")  # 提交信息成功后跳转面试界面

#登录
class LoginView(View):

    def get(self, request):
        return render(request, 'interviewer_login.html')

    def acc_login(self, request):
        if request.method == "GET":
            return render(request, ".html")
        else:
            interview_id = request.POST.get("id")
            interview_name = request.POST.get("name")
            check = self.interviewer_search(interview_id=interview_id, interview_name=interview_name)  # 验证:返回验证对象,失败则是None
            if check == 1:
                return redirect('interviewer_login.html')
            elif check == 2:
                error = "姓名错误"
                return render(request, "interviewer_login.html", {'error': error})
            elif check == 3:
                error = "学号错误"
                return render(request, "interviewer_login.html", {'error': error})

    # 登出
    def acc_logout(self, request):
        # 用户登出，即删除记录登录信息的cookie
        return response('')

    def interviewer_search(self, interview_id, interview_name):
        try:
            id = Interview.objects.filter(interview_id=interview_id)
            name = Interview.objects.filter(interview_name=interview_name)
        except:
            return '没有注册'
        # 查有此人
        if interview_name == name:
            return '1'
        # 姓名不正确
        elif interview_name != name:
            return '2'
        # 学号不正确
        elif interview_id != id:
            return '3'

#申请书
class Audition(View):
    def get(self, request):
        return render(request, 'audition.html')

    def freshman_search(request):
        # 用于模糊搜索新生,可以通过名字或者学号查
        cookie = request.COOKIES.get("user_info", None)
        if cookie:
            cookie = cookie.replace('\'', '\"')
            user_info = json.loads(cookie, strict=False)

            info = user_info.get('info')

            name_list = Freshman.objects.filter(newname__contains=info)
            id_list = Freshman.objects.filter(newstudent_id__contains=info)

            return render({'name': name_list, 'id': id_list})
        else:
            return None

    # 查看新生申请书
    def check_application(self, request):
        newstudent_id = request.POST.get('newstudent_id')
        application = ''
        try:
            application = Freshman.objects.filter(newstudent_id=newstudent_id)
        except:
            pass

        return render({'application' : application})

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

        return render({'data' : '修改成功'})#'修改成功'
