from django.shortcuts import render, get_object_or_404
from apps.projects.services.project_service import ProjectService


def project_detail(request, slug):
    project = get_object_or_404(
        __import__('apps.projects.models.project', fromlist=['Project']).Project,
        slug=slug
    )
    related = ProjectService.get_all_active().exclude(pk=project.pk)[:4]
    context = {
        'project': project,
        'related_projects': related,
    }
    return render(request, 'pages/project_detail.html', context)
