from django.shortcuts import render, redirect

from .models import Blog
from .forms import BlogForm


def blog_create(request):
    form = BlogForm()
    title = request.GET.get('title')
    print(title)
    context = {
        'form': form
    }
    return render(request, 'blog/create.html', context=context)


def list_view(request, *args, **kwargs):
    context = {
        'blog': Blog.objects.all()
    }
    return render(request, 'blog/blog.html', context=context)
