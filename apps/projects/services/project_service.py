from apps.projects.models.project import Project


class ProjectService:

    @staticmethod
    def get_featured():
        """Retorna el proyecto marcado como destacado (SCT APP)."""
        return Project.objects.filter(is_featured=True).first()

    @staticmethod
    def get_carousel_projects():
        """Retorna proyectos para el carrusel, excluyendo el destacado."""
        return Project.objects.filter(
            status='active'
        ).order_by('carousel_order', '-is_featured')

    @staticmethod
    def get_all_active():
        return Project.objects.filter(status='active')

    @staticmethod
    def get_by_slug(slug):
        return Project.objects.prefetch_related('technologies', 'images').get(slug=slug)
