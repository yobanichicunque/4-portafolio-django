from django.db import models

# Create your models here.


class Formacion(models.Model):
    formacion = models.CharField(max_length=150, verbose_name='Título')
    title_obtenido = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha modificación')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']
