from django.contrib import admin
from .models import OrdinaryUser, Administrator
# Register your models here.

admin.site.register(OrdinaryUser)
admin.site.register(Administrator)
admin.site.site_header = '校园二手交易集市系统'
admin.site.site_title = '校园二手交易集市系统'
