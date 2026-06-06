from django.db import models


class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nuevo'),
        ('read', 'Leído'),
        ('replied', 'Respondido'),
        ('archived', 'Archivado'),
    ]

    name = models.CharField(max_length=150, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Correo')
    company = models.CharField(max_length=150, blank=True, verbose_name='Empresa')
    subject = models.CharField(max_length=200, verbose_name='Asunto')
    message = models.TextField(verbose_name='Mensaje')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='new'
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject}'
