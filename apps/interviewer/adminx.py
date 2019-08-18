#coding=utf-8
import xadmin

from apps.interviewer.models import *

xadmin.site.register(Interview)
xadmin.site.register(Question)