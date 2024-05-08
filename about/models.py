from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    degree_title = models.CharField(
        max_length=300, verbose_name='Título obtenido')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha modificación')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'formación'
        verbose_name_plural = 'formaciones'
        ordering = ['-created']


class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='Título')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha modificación')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        ordering = ['-created']
