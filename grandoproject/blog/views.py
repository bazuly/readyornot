from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import ListView
from .forms import CommentForm
from django.views.decorators.http import require_POST


class PostListView(ListView):
    """
    Alternative post_list version,
    right version
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, post, year, month, day):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,

                             publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request, 'blog/post/comment.html',
                  {'post': post,
                   'form': form,
                   'comment': comment})


