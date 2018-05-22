from datetime import datetime
from django.db import models
from courses.models import Course
from users.models import UserProfile
# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=20)
    mobile = models.CharField(verbose_name="手机", max_length=11)
    course_name = models.CharField(verbose_name="课程名", max_length=50)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户查询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    course = models.ForeignKey(Course, verbose_name="课程")
    comments = models.CharField(verbose_name="评论", max_length=200)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    fav_id = models.IntegerField(verbose_name="数据id", default=0)
    fav_type_choice = ((1, '课程'),
                       (2, '课程机构'),
                       (3, '讲师'),
                       )
    fav_type = models.IntegerField(verbose_name="收藏类型", choices=fav_type_choice, default=1)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(verbose_name="接收用户", default=0)
    message = models.CharField(verbose_name="消息内容", max_length=500)
    has_read = models.BooleanField(verbose_name="是否已读", default=False)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    course = models.ForeignKey(Course, verbose_name="课程")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name
