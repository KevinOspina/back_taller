from django.db import models
from django.contrib.auth.models import User, Group
from .extras import GRADE_CHOICES, PRINCIPLE_CHOICES, EVIDENCE_CHOICES


class Instrument(models.Model):
    name = models.CharField(null=False, max_length=100, verbose_name='Nombre')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='instruments',
                              verbose_name='Dueño', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        unique_together = ('name', 'owner')
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'


class Assessment(models.Model):
    """
    An assessment related to an specific user
    """
    instrument = models.OneToOneField(Instrument, on_delete=models.CASCADE, verbose_name='Instrumento')

    def __str__(self):
        return 'Assessment of: %s - %s' % (self.instrument.name, self.instrument.owner)

    class Meta:
        ordering = ['-id']
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"


class Principle(models.Model):
    """
    Principle composing an assessment
    """
    principle = models.CharField(max_length=30, null=False, choices=PRINCIPLE_CHOICES, verbose_name='Principio')
    grade = models.CharField(max_length=30, null=False, choices=GRADE_CHOICES, verbose_name='Nivel')
    justification = models.CharField(max_length=150, null=False, verbose_name='Justificación')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='principles', verbose_name='Evaluación')

    class Meta:
        ordering = ['-id']
        verbose_name = "Principio"
        verbose_name_plural = "Principios"
        unique_together = ("assessment", "principle")

    def __str__(self):
        return '{}: {}'.format(self.principle, self.justification)


class Component(models.Model):
    description = models.TextField(verbose_name='Nombre')
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name='components', verbose_name='Instrumento')
    component_type = models.CharField(max_length=20, choices=EVIDENCE_CHOICES, verbose_name='Tipo')

    def __str__(self):
        return '{}: {}'.format(self.component_type, self.description)

    class Meta:
        ordering = ['-id']
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"


class Evidence(models.Model):
    """
    Represents all the evidence of a principle on an strategy
    """
    principle = models.ForeignKey(Principle, on_delete=models.CASCADE, related_name='evidences', verbose_name='Principio')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, verbose_name='Componente')

    def __str__(self):
        return '{}: {}'.format(self.principle.principle, self.component.description)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Evidencias'
        verbose_name = 'Evidencia'
        unique_together = ('principle', 'component')
