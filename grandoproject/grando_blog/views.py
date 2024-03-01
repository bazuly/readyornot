from django.shortcuts import render
from grando_blog.models import Post, Comment


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        'posts': posts
    }

    return render(request, 'template/grando_blog/index.html', context)


def blog_category(requset, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")

    context = {
        'category': category,
        'posts': posts,
    }

    return render(requset, 'template/grando_blog/category.html', context)


def blog_detail(request, pk):
    post = Post.objects.all(pk=pk)
    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments
    }

    return render(request, 'template/detail.html', context)


