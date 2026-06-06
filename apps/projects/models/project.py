from django.db import models
from django.utils.text import slugify
from .technology import Technology


class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('development', 'En desarrollo'),
        ('archived', 'Archivado'),
    ]

    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    subtitle = models.CharField(max_length=300, blank=True, verbose_name='Subtítulo')
    description = models.TextField(verbose_name='Descripción')
    short_description = models.CharField(
        max_length=250, blank=True,
        verbose_name='Descripción corta (para cards)'
    )

    # Proyecto principal (SCT APP)
    is_featured = models.BooleanField(
        default=False, verbose_name='Proyecto destacado',
        help_text='Solo un proyecto debe ser destacado a la vez'
    )

    # Imagen de portada
    cover_image = models.ImageField(
        upload_to='projects/covers/', blank=True, null=True,
        verbose_name='Imagen de portada'
    )

    technologies = models.ManyToManyField(
        Technology, blank=True, verbose_name='Tecnologías'
    )

    # Métricas del proyecto
    users_count = models.PositiveIntegerField(
        default=0, verbose_name='Usuarios activos',
        help_text='Número aproximado de usuarios'
    )
    duration_months = models.PositiveSmallIntegerField(
        default=0, verbose_name='Duración (meses)'
    )

    # Links externos
    url_live = models.URLField(blank=True, verbose_name='URL en producción')
    url_repo = models.URLField(blank=True, verbose_name='URL repositorio')

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='active',
        verbose_name='Estado'
    )

    # Orden en carrusel
    carousel_order = models.PositiveSmallIntegerField(
        default=0, verbose_name='Orden en carrusel'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-is_featured', 'carousel_order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_cover_url(self):
        if self.cover_image:
            return self.cover_image.url
        return '/static/img/projects/default.jpg'
