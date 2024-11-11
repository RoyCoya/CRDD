from django.urls import path

from . import views

app_name = 'MainFrame'

# 页面
pages = [
	path('', views.homepage, name='homepage'),
    path('test/', views.TestAPIView.as_view(), name='test_api'),
    path('login/', views.LoginView.as_view(), name='login'),
]

urlpatterns = pages
# urlpatterns += apis