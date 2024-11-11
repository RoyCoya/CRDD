from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


djangoURLs = [
    # admin后台
    path('admin/', admin.site.urls),
    # 用户模板
    path('accounts/', include('django.contrib.auth.urls')),
]

jwtURLs = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
    
publicAPPs = [
    path('', include('MainFrame.urls')),
    path('ontology/', include('OntologyBase.urls')),
]

privateAPPs = [
    
]

urlpatterns = djangoURLs + publicAPPs + privateAPPs + jwtURLs

# 开发时可显示用户文件
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^userfile/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]