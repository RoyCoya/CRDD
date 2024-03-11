from django.urls import path

from . import views

app_name = 'MainFrame'

# 页面
pages = [
	path('', views.homepage, name='homepage'),
    path('test/', views.TestAPIView.as_view(), name='test_api')
]

# 接口
# apis = [
# 	path('api_index/', views.api_index, name=''),
# ]

urlpatterns = pages
# urlpatterns += apis