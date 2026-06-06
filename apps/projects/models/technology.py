from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Tecnología')
    slug = models.SlugField(max_length=80, unique=True)
    icon_class = models.CharField(
        max_length=100, blank=True,
        help_text='Clase CSS del ícono (devicons, simple-icons, etc.)'
    )
    color = models.CharField(
        max_length=7, default='#D4AF37',
        help_text='Color hexadecimal para el badge'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Tecnología'
        verbose_name_plural = 'Tecnologías'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
