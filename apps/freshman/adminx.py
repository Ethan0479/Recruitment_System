#coding=utf-8
#改为
import xadmin
from xadmin import views
from .models import *

# Register your models here.
xadmin.site.register(Freshman)
xadmin.site.register(Academy)
xadmin.site.register(Major)