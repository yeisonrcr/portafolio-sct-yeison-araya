from django.shortcuts import render
from apps.blog.services.blog_service import BlogService


def blog_list(request):
    context = {
        'posts': BlogService.get_published(),
        'categories': BlogService.get_categories(),
    }
    return render(request, 'pages/blog_list.html', context)
