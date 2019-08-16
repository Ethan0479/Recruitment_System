#coding=utf-8
#改为
import xadmin
from xadmin import views
from .models import Freshman

# Register your models here.
xadmin.site.register(Freshman)
# class RecordAdmin(object):
#     data_charts = {
#         "user_count": {'title': u"User Report", "x-field": "date", "y-field": ("user_count", "view_count"), "order": ('date',)},
#         "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
#     }