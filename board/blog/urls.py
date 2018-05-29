from django.urls import re_path

from board.blog.views import PostList, PostDetail, PostCreate, update

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', PostList.as_view(), name='home'),
    re_path(r'^create/$', PostCreate.as_view(), name='create'),
    re_path(r'(?P<pk>\d+)/$', PostDetail.as_view(), name='detail'),
    re_path(r'(?P<pk>\d+)/update$', update, name='update')
]
