from django.db import models
from django.utils.text import slugify
from .category import Category


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    ]

    title = models.CharField(max_length=250, verbose_name='Título')
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='posts'
    )
    excerpt = models.CharField(
        max_length=350, blank=True, verbose_name='Extracto'
    )
    content = models.TextField(verbose_name='Contenido')
    cover_image = models.ImageField(
        upload_to='blog/covers/', blank=True, null=True,
        verbose_name='Imagen de portada'
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft'
    )
    reading_time = models.PositiveSmallIntegerField(
        default=5, verbose_name='Tiempo de lectura (minutos)'
    )
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
