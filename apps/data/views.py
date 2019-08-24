import random

from django.shortcuts import render
from ..freshman import models
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
        if num == '':
            return render(request, 'manage.html', {'msg': '错误'})
        else:
            num = int(num)
            name_date1 = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张鲁韦昌马苗凤花方'  # 32
            # 152
            name_date2 = ['子墨', '铧隆', '清发', '紫涵', '子萱', '天佑', '紫宸', '紫辰', '祥儒', '祥涵', '芷晴', '婉婷', '语嫣', '玉涵', '倩雪', '钰', '钰彤', '漪', '淑郡', '淑君', '洁玉', '溪儿', '滢', '梓涵', '素昕', '昕珏', '琼玉', '漩', '梓漩', '友泽', '潇彬', '楚缳', '誉', '婉仪', '清发', '泊君', '琪凌', '楚汐', '楚沣', '楚淇', '楚洋', '晓丹', '清云', '青芸', '党险', '砾铎', '君钧', '钧', '麟英', '麟雁', '雁', '静', '凡东', '啸雄', '启航', '文豪', '锦彬', '毅豪', '晨豪', '君豪', '骏豪', '可琪', '明豪', '昱雄', '发', '清妍', '晨皓', '旭', '雨轩', '淑瑜', '淑萱', '健邦', '汉城', '才洪', '子轩', '令晨', '子鉴', '庆润', '炫荧', '炫莹', '炫', '梓炫', '紫炫', '芷炫', '庆焮', '耀财', '家达', '恩彤', '浩熙', '安琪', '浩', '浩骏', '浩鹏', '浩升', '熙茹', '南瓜', '冬瓜', '地瓜', '土豆', '华藤', '花藤', '文博', '文昊', '俊文', '智涵', '菀柳', '京平', '煜培', '思远', '炜昊', '若宣', '泽罡', '泽宇', '泽旭', '雅丽', '泽轩', '泽昊', '昊铭', '铭昊', '铭峰', '玮峰', '玮昊', '泽程', '翔昊', '卓昊', '玉英', '一丹', '子届', '凡长', '淼', '子朗', '芷暄', '顺', '海维', '子晏', '子彦', '钰涵', '梓轩', '晓艳', '涛', '莉', '秀梅', '诗雅', '伟', '子酿', '发强', '惠华', '星瑶', '晨曦', '星泽', '星睿', '思旗']
            provinces = ['北京市', '天津市', '上海市', '重庆市', '河北市', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省','河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海', '台湾', '内蒙古自治区', '广西壮族自治区','西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区']
            direction = ['设计','设计','开发','秘书处','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发','开发']
            for i in range(0, num):

                a1 = random.randint(0, 31)
                a2 = random.randint(0, 151)
                a3 = random.randint(0, 100)  # 性别参数
                a4 = random.randint(1, 26)  # 学院
                a5 = random.randint(0, 33)  # 省份
                a7 = random.randint(1, 15)  # 班级
                a8 = random.randint(100000000,999999999) #手机号 qq号
                a9 = random.randint(0,22)  #方向
                student = models.Freshman()
                student.newstudent_id = str(2019000000+i)
                student.newname = name_date1[a1]+name_date2[a2]
                student.password = '123456'
                if (a2+a3) % 2 == 0:
                    student.gender = '男'
                else:
                    student.gender = '女'
                print(a4)
                if a4 == 20:
                    student.college = models.Academy.objects.get(id=str(19))
                    majors = models.Major.objects.filter(majorAcademy=str(19))
                else:
                    student.college = models.Academy.objects.get(id=str(a4))
                    majors = models.Major.objects.filter(majorAcademy=str(a4))
                a6 = random.randint(0,len(majors)-1)
                student.major = majors[a6]
                student.newclass = str(1900+a7)

                student.phone = str(13+a8)
                student.qq = str(a8)
                student.email = str(a8)+'@qq.com'
                student.direction = direction[a9]
                # 预约时间 申请书 面试时间 面试地点 得分 评价 面试结果 面试官姓名 公寓楼 宿舍号 验证码
                student.province = provinces[a5]
                student.save()
            return render(request,'manage.html',{'msg':'数据生成完成'})


