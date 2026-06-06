from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.projects.serializers.project_serializer import (
    ProjectListSerializer, ProjectDetailSerializer, TechnologySerializer
)
from apps.blog.serializers.blog_serializer import BlogPostSerializer, BlogPostDetailSerializer
from apps.cases.serializers.case_serializer import CaseStudySerializer
from apps.contact.serializers.contact_serializer import ContactMessageSerializer
from rest_framework import viewsets, generics, permissions
from apps.projects.models.project import Project
from apps.projects.models.technology import Technology
from apps.blog.models.post import BlogPost
from apps.cases.models.case_study import CaseStudy
from apps.contact.models.contact_message import ContactMessage


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(status='active').prefetch_related('technologies', 'images')
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectListSerializer


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(status='published')
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        return BlogPostSerializer


class CaseStudyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseStudy.objects.filter(is_published=True)
    serializer_class = CaseStudySerializer
    lookup_field = 'slug'


class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else self.request.META.get('REMOTE_ADDR')
        serializer.save(ip_address=ip)


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'technologies', TechnologyViewSet, basename='technology')
router.register(r'blog', BlogPostViewSet, basename='blog')
router.register(r'cases', CaseStudyViewSet, basename='case')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactCreateView.as_view(), name='api-contact'),
]
