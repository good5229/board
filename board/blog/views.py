from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView

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


def update(request, pk):
    if request.method == "POST":
        # 수정 저장
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post)
    else:
        # 수정 입력
        post = Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        return render(request, 'create.html', {'object': post, 'form': form})
