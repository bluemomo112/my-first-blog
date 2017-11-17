from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

'''
匹配 ^（表示开头）并紧随 $ （表示结尾），所以只有空字符串会被匹配到,
这是正确的，因为在 Django 的 URL 解析器中，'http://127.0.0.1:8000/' 并不是 URL 的一部分。
（译注：即只有 'http://127.0.0.1:8000/' 后面的部分会被解析。
如果后面的部分为空，即是空字符串被解析。） 
这个模式告诉了 Django，
如果有人访问 'http://127.0.0.1:8000' 地址，那么 views.post_list 是这个请求该去到的地方。
'''
