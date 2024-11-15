from django.urls import path

from . import views

app_name = 'MainFrame'

# 页面
pages = [
	path('', views.homepage, name='homepage'),
    path('test/', views.TestAPI.as_view(), name='test_api'),
    path('login/', views.Login.as_view(), name='login'),
    path('users/', views.UserInfo.as_view(), name='login'),
]

urlpatterns = pages
# urlpatterns += apis