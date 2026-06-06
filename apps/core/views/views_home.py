from django.shortcuts import render
from apps.projects.services.project_service import ProjectService
from apps.cases.models.case_study import CaseStudy
from apps.blog.models.post import BlogPost


def home(request):
    context = {
        'featured_project': ProjectService.get_featured(),
        'carousel_projects': ProjectService.get_carousel_projects(),
        'cases': CaseStudy.objects.filter(is_published=True).order_by('order')[:3],
        'latest_posts': BlogPost.objects.filter(status='published').order_by('-published_at')[:3],
    }
    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')
