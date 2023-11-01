from django.db import models


# Create your models here.
class OrdinaryUser(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name='用户编号')
    user_name = models.CharField(max_length=20, verbose_name='用户昵称')
    user_password = models.CharField(max_length=20, verbose_name='用户密码')
    user_email = models.CharField(max_length=20, verbose_name='用户邮箱')  # Field name made lowercase.
    accountStatus = models.IntegerField(choices=[(1, '正常'), (0, '已封禁')],
                                        verbose_name='AccountStatus')  # Field name made lowercase.

    class Meta:
        ordering = ['user_id']
        db_table = 'OrdinaryUser'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True, verbose_name='管理员编号')
    admin_name = models.CharField(max_length=20, verbose_name='管理员昵称')  # Field name made lowercase.
    admin_password = models.CharField(max_length=20, verbose_name='管理员密码')
    admin_email = models.CharField(max_length=20, verbose_name='管理员邮箱')  # Field name made lowercase.

    class Meta:
        ordering = ['admin_id']
        db_table = 'Administrator'
        verbose_name = "管理员信息"
        verbose_name_plural = verbose_name
