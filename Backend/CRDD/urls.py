from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

djangoURLs = [
    # admin后台
    path('admin/', admin.site.urls),
    # 用户模板
    path('accounts/', include('django.contrib.auth.urls')),
]
    
publicAPPs = [
    path('', include('MainFrame.urls')),
]

privateAPPs = [
    
]

urlpatterns = djangoURLs + publicAPPs + privateAPPs

# 开发时可显示用户文件
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^userfile/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]