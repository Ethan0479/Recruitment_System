from django.db import models

# Create your models here.
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from django.db import models
# class Data(models.Model):
#     info = models.CharField(max_length=255)
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# bar.render()
#
#
# x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# y = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图示例")
# pie.add("", x, y, is_label_show=True)
# pie.render()