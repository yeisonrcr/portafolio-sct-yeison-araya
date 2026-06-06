from django.db import models
from .project import Project


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='images', verbose_name='Proyecto'
    )
    image = models.ImageField(
        upload_to='projects/gallery/', verbose_name='Imagen'
    )
    caption = models.CharField(
        max_length=200, blank=True, verbose_name='Descripción'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Imagen del proyecto'
        verbose_name_plural = 'Imágenes del proyecto'
        ordering = ['order']

    def __str__(self):
        return f'{self.project.title} — imagen {self.order}'
