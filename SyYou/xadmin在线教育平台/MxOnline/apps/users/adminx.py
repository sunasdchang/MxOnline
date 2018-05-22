import xadmin
# 创建xadmin的最基本管理器配置，并与view绑定
from xadmin import views    # 导入xadmin的views
from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row


class BaseSetting(object):
    #开启主题功能
    enable_themes = True     # 主题管理器
    use_bootswatch = True    # 使用主题


# 头部系统名称和底部版权管理器
class GlobalSettings(object):
    site_title = '胜优后台管理系统'  # 头部系统名称
    site_footer = '胜优教育公司'  # 底部版权
    menu_style = 'accordion'  #收起导航栏，折叠每个app


class EmailVerifyRecordAdmin(object):
    """
    用户邮箱
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fas fa-envelope'


class BannerAdmin(object):
    """
    轮播图
    """
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# xadmin.site.unregister(User)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)  # 将主题管理器绑定views.BaseAdminView注册
xadmin.site.register(views.CommAdminView, GlobalSettings)  # 头部系统名称和底部版权管理器绑定views.CommAdminView注册