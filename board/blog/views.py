from django.views.generic import ListView, DetailView, CreateView, UpdateView

from board.blog.forms import PostForm
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreate(CreateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
