from django.shortcuts import render, get_object_or_404
from apps.blog.models.post import BlogPost


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    related = BlogPost.objects.filter(
        status='published', category=post.category
    ).exclude(pk=post.pk)[:3]
    context = {'post': post, 'related': related}
    return render(request, 'pages/blog_detail.html', context)
