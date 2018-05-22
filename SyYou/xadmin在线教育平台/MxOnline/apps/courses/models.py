from datetime import datetime
from DjangoUeditor.models import UEditorField
from django.db import models
from organization.models import CourseOrg, Teacher
# Create your models here.


class Course(models.Model):
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    detail = UEditorField(verbose_name="课程详情", width=600, height=300, imagePath="courses/ueditor/", filePath="courses/ueditor/", default='')
    degree_choices = (('cj', '初级'),
                      ('zj', '中级'),
                      ('gj', '高级'),
                      )
    degree = models.CharField(verbose_name="难度", choices=degree_choices, max_length=2)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    image = models.ImageField(verbose_name="封面图", upload_to="courses/%Y/%m", max_length=100)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    tag = models.CharField(verbose_name="课程标签", default="", max_length=10)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)
    course_org = models.ForeignKey(CourseOrg, verbose_name="所属机构", null=True, blank=True)
    category = models.CharField(verbose_name="课程类别", max_length=20, default="")
    teacher = models.ForeignKey(Teacher, verbose_name="讲师", null=True, blank=True)
    youneed_know = models.CharField(verbose_name="课程须知", max_length=300, default='')
    teacher_tell = models.CharField(verbose_name="老师告诉你", max_length=300, default='')
    is_banner = models.BooleanField(verbose_name="是否轮播", default=False)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程的章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章节数"  # 在后台显示的名

    def go_to(self):
        from django.utils.safestring import mark_safe
        # mark_safe后就不会转义
        return mark_safe("<a href='https://home.cnblogs.com/u/sun1994/'>跳转</a>")

    go_to.short_description = "跳转"

    def get_course_lesson(self):
        #获取课程的章节数
        return self.lesson_set.all()

    def get_learn_users(self):
        # 获取这门课程的学习用户
        return self.usercourse_set.all()[:5]

    def __str__(self):
        return self.name


class BannerCourse(Course):
    """
    显示轮播课程
    """
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(verbose_name="章节名", max_length=100)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        #获取章节所有视频
        return self.video_set.all()

    def __str__(self):
        return '{0}({1})'.format(self.course, self.name)


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(verbose_name="视频名", max_length=100)
    url = models.CharField(verbose_name="访问地址", default="", max_length=200)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(verbose_name="名称", max_length=100)
    download = models.FileField(verbose_name="资源文件", upload_to="course/resource/%Y/%m", max_length=100)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name
