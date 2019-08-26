import random

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from ..freshman import models
from apps.freshman.models import Freshman
import operator
import random

# Create your views here.
def bar1(request):
    return render(request,'render.html')

def bar3(request):
    return None

def bar2(request):
    return None



def manage(request):
    if request.method == "GET":
        return render(request,'manage.html')
    else:
        num = request.POST.get('num','')
        print(num)
        try:
            num = int(num)
            name_date1 = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张鲁韦昌马苗凤花方'  # 32
            # 152
            name_date2 = ['子墨', '铧隆', '清发', '紫涵', '子萱', '天佑', '紫宸', '紫辰', '祥儒', '祥涵', '芷晴', '婉婷', '语嫣', '玉涵', '倩雪', '钰',
                          '钰彤', '漪', '淑郡', '淑君', '洁玉', '溪儿', '滢', '梓涵', '素昕', '昕珏', '琼玉', '漩', '梓漩', '友泽', '潇彬', '楚缳',
                          '誉', '婉仪', '清发', '泊君', '琪凌', '楚汐', '楚沣', '楚淇', '楚洋', '晓丹', '清云', '青芸', '党险', '砾铎', '君钧', '钧',
                          '麟英', '麟雁', '雁', '静', '凡东', '啸雄', '启航', '文豪', '锦彬', '毅豪', '晨豪', '君豪', '骏豪', '可琪', '明豪', '昱雄',
                          '发', '清妍', '晨皓', '旭', '雨轩', '淑瑜', '淑萱', '健邦', '汉城', '才洪', '子轩', '令晨', '子鉴', '庆润', '炫荧', '炫莹',
                          '炫', '梓炫', '紫炫', '芷炫', '庆焮', '耀财', '家达', '恩彤', '浩熙', '安琪', '浩', '浩骏', '浩鹏', '浩升', '熙茹', '南瓜',
                          '冬瓜', '地瓜', '土豆', '华藤', '花藤', '文博', '文昊', '俊文', '智涵', '菀柳', '京平', '煜培', '思远', '炜昊', '若宣',
                          '泽罡', '泽宇', '泽旭', '雅丽', '泽轩', '泽昊', '昊铭', '铭昊', '铭峰', '玮峰', '玮昊', '泽程', '翔昊', '卓昊', '玉英',
                          '一丹', '子届', '凡长', '淼', '子朗', '芷暄', '顺', '海维', '子晏', '子彦', '钰涵', '梓轩', '晓艳', '涛', '莉', '秀梅',
                          '诗雅', '伟', '子酿', '发强', '惠华', '星瑶', '晨曦', '星泽', '星睿', '思旗']
            provinces = ['北京', '天津', '上海', '重庆', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建',
                         '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '台湾',
                         '内蒙古', '广西', '西藏', '宁夏', '新疆', '香港', '澳门']
            direction = ['设计', '设计', '开发', '秘书处', '开发', '开发', '开发', '开发', '开发', '开发', '开发', '开发', '开发', '开发', '开发',
                         '开发', '开发', '开发', '开发', '开发', '开发', '开发', '开发']
            for i in range(0, num):

                a1 = random.randint(0, 31)
                a2 = random.randint(0, 151)
                a3 = random.randint(0, 100)  # 性别参数
                a4 = random.randint(1, 26)  # 学院
                a5 = random.randint(0, 33)  # 省份
                a7 = random.randint(1, 15)  # 班级
                a8 = random.randint(100000000, 999999999)  # 手机号 qq号
                a9 = random.randint(0, 22)  # 方向
                student = models.Freshman()
                student.newstudent_id = str(2019000000 + i)
                student.newname = name_date1[a1] + name_date2[a2]
                student.password = '123456'
                if (a2 + a3) % 2 == 0:
                    student.gender = '男'
                else:
                    student.gender = '女'
                if a4 == 20:
                    student.college = models.Academy.objects.get(id=str(19))
                    majors = models.Major.objects.filter(majorAcademy=str(19))
                else:
                    student.college = models.Academy.objects.get(id=str(a4))
                    majors = models.Major.objects.filter(majorAcademy=str(a4))
                a6 = random.randint(0, len(majors) - 1)
                student.major = majors[a6]
                student.newclass = str(1900 + a7)

                student.phone = str(13 + a8)
                student.qq = str(a8)
                student.email = str(a8) + '@qq.com'
                student.direction = direction[a9]
                # 预约时间 申请书 面试时间 面试地点 得分 评价 面试结果 面试官姓名 公寓楼 宿舍号 验证码
                student.province = provinces[a5]
                student.save()
            print(1)
            return HttpResponse('数据生成完成')
        except:
            print(0)
            return HttpResponse('数据生成出错，请输入数字')


def timedata(request):
    if request.method =="POST":
        date = request.POST.get('date', '')
        dateList = date.split('@')
        dateList.remove('')
        stus = models.Freshman.objects.all()
        for stu in stus:
            a1 = random.randint(0, len(dateList)-1)
            a2 = random.randint(0, len(dateList)-1)
            a3 = random.randint(0, len(dateList)-1)
            stu.appointment_one = dateList[a1]
            stu.appointment_two = dateList[a2]
            stu.appointment_three = dateList[a3]
            stu.save()
        return HttpResponse("成功")
    else:
        return HttpResponse("错误")


def appoint_interview_time(request):
    #month = request.POST.get("month", '')
    #day = request.POST.get("day", '')
    #month = ('09-24_','09-25_','09-26_','09-27_','09-28_','09-29_','09-30_')
    month = ('9-27_','9-28_','9-29_','9-30_','9-31_','10-1_','10-2_')
    month_len = len(month)
    day = ('8:00-10:00','10:00-12:00','14:00-16:00','16:00-18:00','19:00-21:00')
    day_len = len(day)

    interview_day = {}
    for a in range(month_len):
        for b in range(day_len):
            interview_day[month[a]+day[b]] = random.randint(65,120)

    # interview_day = {"9-27_8:00-10:00": 85, "9-27_10:00-12:00": 90, "9-27_14:00-16:00": 90, "9-27_16:00-18:00": 90,"9-27_19:00-21:00": 70,
    #                  "9-28_8:00-10:00": 75, "9-28_10:00-12:00": 50, "9-28_14:00-16:00": 100, "9-28_16:00-18:00": 110,"9-28_19:00-21:00": 70,
    #                  "9-29_8:00-10:00": 95, "9-29_10:00-12:00": 130, "9-29_14:00-16:00": 100, "9-29_16:00-18:00": 70,"9-29_19:00-21:00": 120,
    #                  "9-30_8:00-10:00": 65, "9-30_10:00-12:00": 70, "9-30_14:00-16:00": 100, "9-30_16:00-18:00": 110,"9-30_19:00-21:00": 110,
    #                  "9-31_8:00-10:00": 110, "9-31_10:00-12:00": 115, "9-31_14:00-16:00": 40, "9-31_16:00-18:00": 80,"9-31_19:00-21:00": 90,
    #                  "10-1_8:00-10:00": 90, "10-1_10:00-12:00": 70, "10-1_14:00-16:00": 110, "10-1_16:00-18:00": 70,"10-1_19:00-21:00": 90,
    #                  "10-2_8:00-10:00": 90, "10-2_10:00-12:00": 110, "10-2_14:00-16:00": 90, "10-2_16:00-18:00": 90,"10-2_19:00-21:00": 90,
    #                  }

    sum = 0
    for a in range(month_len):
        for b in range(day_len):
            sum += interview_day[month[a]+day[b]]

    # if interview_day == '':
    #     return '请输入面试时间'
    all_student = Freshman.objects.all()
    all_student_appointmenttime = [0 for a in range(len(all_student))]
    for a in range(len(all_student)):
        all_student_appointmenttime[a] = {"newstudent_id":all_student[a].newstudent_id,"appointment_one":
            all_student[a].appointment_one, "appointment_two" : all_student[a].appointment_two,
                                          "appointment_three":all_student[a].appointment_three}

    #建立空字典列表，每个字典的值为列表，储存学生id
    all_time_student = {}
    for a in range(month_len):
        for b in range(day_len):
            all_time_student[month[a]+day[b]] = []

    appointment_list = ['appointment_one', 'appointment_two', 'appointment_three']
    #面试预约时间
    for appointment in appointment_list:
        for a in range(len(all_student_appointmenttime)):
            if a >= len(all_student_appointmenttime):break
            appointmenttime = all_student_appointmenttime[a][appointment]
            if len(all_time_student[appointmenttime]) <= interview_day[appointmenttime]:
                all_time_student[appointmenttime].append(all_student_appointmenttime.pop(a))
    #安排剩下的学生，如果一次循环不行那就两次，不行就三次
    for i in range(2):
        for a in range(len(all_student_appointmenttime)):
            for appointment in appointment_list:
                if a >= len(all_student_appointmenttime): break
                appointmenttime = all_student_appointmenttime[a][appointment]
                for b in range(len(all_time_student[appointmenttime])):
                    for appoint in appointment_list:
                        if b >= len(all_time_student[appointmenttime]): break
                        select_time = all_time_student[appointmenttime][b]
                        select = select_time[appoint]
                        if len(all_time_student[select]) <= interview_day[select]:
                            all_time_student[select].append(all_time_student[appointmenttime].pop(b))
                            if a >= len(all_student_appointmenttime): break
                            all_time_student[appointmenttime].append(all_student_appointmenttime.pop(a))
    #将数据存到数据库中
    freshmansave = Freshman()
    for a in month:
        for b in day:
            for student in all_time_student[a+b]:
                newstudent_id = student['newstudent_id']
                student_one = Freshman.objects.get(newstudent_id=newstudent_id)
                student_one.interview_time = a+b
                student_one.save()

    return render_to_response('test.html', {'all_time_student':all_time_student, 'all_student_appointmenttime':all_student_appointmenttime,
                                            'sum':sum})



