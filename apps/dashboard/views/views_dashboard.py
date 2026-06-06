from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.dashboard.services.stats_service import StatsService


@login_required
def dashboard_home(request):
    context = StatsService.get_summary()
    return render(request, 'pages/dashboard.html', context)
