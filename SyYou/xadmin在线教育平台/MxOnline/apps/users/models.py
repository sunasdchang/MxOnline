from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户信息
    """
    nick_name = models.CharField(max_length=64, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", blank=True, null=True)
    gender_choices = (('male', '男'),
                      ('female', '女'),
                      )
    gender = models.CharField(verbose_name="性别", choices=gender_choices, max_length=15, default='female')
    address = models.CharField(verbose_name="地址", max_length=100, default="")
    mobile = models.CharField(verbose_name="手机号", max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def unread_nums(self):
        #获取用户未读消息的数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class EmailVerifyRecord(models.Model):
    """
    邮箱验证
    """
    code = models.CharField(verbose_name="验证码", max_length=20)
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    send_choices = (('register', '注册'),
                    ('forget', '找回密码'),
                    ('update_email', '修改邮箱')
                    )
    send_type = models.CharField(verbose_name="验证码类型", choices=send_choices, max_length=30)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    """
    轮播图
    """
    title = models.CharField(verbose_name="标题", max_length=100)
    image = models.ImageField(verbose_name="轮播图", upload_to='banner/%Y/%m', max_length=500)
    url = models.URLField(verbose_name="访问地址", max_length=200)
    index = models.IntegerField(verbose_name="顺序", default=100)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


