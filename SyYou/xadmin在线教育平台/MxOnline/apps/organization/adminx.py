
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    """
    城市
    """
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    """
    机构
    """
    list_display = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'students', 'course_nums', 'image',
                    'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'students', 'course_nums', 'image',
                     'address', 'city']
    list_filter = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'students', 'course_nums', 'image',
                   'address', 'city', 'add_time']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    """老师"""
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                    'fav_nums', 'add_time', 'image']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                     'fav_nums', 'image']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums',
                   'fav_nums', 'add_time', 'image']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
