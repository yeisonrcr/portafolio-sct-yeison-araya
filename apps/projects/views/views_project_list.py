from django.shortcuts import render
from apps.projects.services.project_service import ProjectService


def project_list(request):
    context = {
        'projects': ProjectService.get_all_active(),
        'featured': ProjectService.get_featured(),
    }
    return render(request, 'pages/projects.html', context)
