from django.shortcuts import render, get_object_or_404
from apps.cases.models.case_study import CaseStudy


def case_detail(request, slug):
    case = get_object_or_404(CaseStudy, slug=slug, is_published=True)
    return render(request, 'pages/case_detail.html', {'case': case})
