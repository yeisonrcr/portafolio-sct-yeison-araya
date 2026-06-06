from django.db import models
from django.utils.text import slugify


class CaseStudy(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    industry = models.CharField(max_length=100, blank=True, verbose_name='Industria')
    company_size = models.CharField(
        max_length=100, blank=True,
        verbose_name='Tamaño de empresa'
    )
    problem = models.TextField(verbose_name='Problema')
    solution = models.TextField(verbose_name='Solución')
    result = models.TextField(verbose_name='Resultado')
    metric_1_label = models.CharField(max_length=80, blank=True)
    metric_1_value = models.CharField(max_length=80, blank=True)
    metric_2_label = models.CharField(max_length=80, blank=True)
    metric_2_value = models.CharField(max_length=80, blank=True)
    metric_3_label = models.CharField(max_length=80, blank=True)
    metric_3_value = models.CharField(max_length=80, blank=True)
    is_published = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Caso de éxito'
        verbose_name_plural = 'Casos de éxito'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
