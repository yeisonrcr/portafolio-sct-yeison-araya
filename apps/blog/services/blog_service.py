from apps.blog.models.post import BlogPost
from apps.blog.models.category import Category


class BlogService:

    @staticmethod
    def get_published():
        return BlogPost.objects.filter(status='published').order_by('-published_at')

    @staticmethod
    def get_by_slug(slug):
        return BlogPost.objects.get(slug=slug, status='published')

    @staticmethod
    def get_categories():
        return Category.objects.all()
