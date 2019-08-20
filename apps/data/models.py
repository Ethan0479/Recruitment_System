from django.db import models

# Create your models here.
# from pyecharts import Bar
# from pyecharts import Pie
from django.db import models
class Data(models.Model):
    info = models.CharField(max_length=60)

    class Mate:
        verbose_name = u'数据'
        verbose_name_plural = u'数据'


# bar =Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.show_config()
# bar.render()

# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[11, 12, 13, 10, 10, 10]
# pie =Pie("饼图示例")
# pie.add("", attr, v1, is_label_show=True)
# pie.show_config()
# pie.render()