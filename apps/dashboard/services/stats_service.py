from apps.projects.models.project import Project
from apps.blog.models.post import BlogPost
from apps.cases.models.case_study import CaseStudy
from apps.contact.models.contact_message import ContactMessage


class StatsService:

    @staticmethod
    def get_summary():
        return {
            'total_projects': Project.objects.filter(status='active').count(),
            'total_posts': BlogPost.objects.filter(status='published').count(),
            'total_cases': CaseStudy.objects.filter(is_published=True).count(),
            'new_messages': ContactMessage.objects.filter(status='new').count(),
            'total_messages': ContactMessage.objects.count(),
            'recent_messages': ContactMessage.objects.order_by('-created_at')[:5],
        }
