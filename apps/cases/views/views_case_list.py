from django.shortcuts import render
from apps.cases.models.case_study import CaseStudy


def case_list(request):
    cases = CaseStudy.objects.filter(is_published=True).order_by('order')
    return render(request, 'pages/cases.html', {'cases': cases})
