from django.urls import re_path, path

from board.blog.views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', PostList.as_view(), name='home'),
    re_path(r'^create/$', PostCreate.as_view(), name='create'),
    re_path(r'(?P<pk>\d+)/$', PostDetail.as_view(), name='detail'),
    re_path(r'(?P<pk>\d+)/update$', PostUpdate.as_view(), name='update'),
    re_path(r'(?P<pk>\d+)/delete$', PostDelete.as_view(), name='delete'),
    # path('', PostComment.as_view(), name='comment'),
]
