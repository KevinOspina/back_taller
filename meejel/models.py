from django.db import models
from django.contrib.auth.models import User, Group
from .extras import GRADE_CHOICES, PRINCIPLE_CHOICES, EVIDENCE_CHOICES, GRADE_LEVEL


class Instrument(models.Model):
    name = models.CharField(null=False, max_length=100, verbose_name='Nombre')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='instruments',
                              verbose_name='Dueño', null=True)

    def level(self):
        total = 0
        for i in self.principles.all():
            total += i.weight
        return total / 50

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        unique_together = ('name', 'owner')
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'


class Principle(models.Model):
    """
    Principle composing an instrument
    """
    principle = models.CharField(max_length=30, null=False, choices=PRINCIPLE_CHOICES, verbose_name='Principio')
    grade = models.CharField(max_length=30, null=False, choices=GRADE_CHOICES, verbose_name='Nivel')
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name='principles', verbose_name='Instrumento')

    @property
    def weight(self):
        x = Evidence.objects.filter(component__instrument=self.instrument, component__component_type='Objetivos').count()
        n = Evidence.objects.filter(principle=self, component__component_type='Objetivos').count()
        tlg = (40 * x) / n if n > 0 else 0
        y = Evidence.objects.filter(component__instrument=self.instrument, component__component_type='Reglas').count()
        m = Evidence.objects.filter(principle=self, component__component_type='Reglas').count()
        tru = (30 * y) / m if m > 0 else 0
        tro = Evidence.objects.filter(principle=self, component__component_type='Roles').count()
        tma = Evidence.objects.filter(principle=self, component__component_type='Materiales').count()
        tst = Evidence.objects.filter(principle=self, component__component_type='Pasos').count()
        r = 10 if tro > 0 else 0
        s = 5 if tst > 0 else 0
        m = 5 if tma > 0 else 0
        return (r + s + m + tru + tlg) * GRADE_LEVEL[self.grade]

    class Meta:
        ordering = ['-id']
        verbose_name = "Principio"
        verbose_name_plural = "Principios"
        unique_together = ("instrument", "principle")

    def __str__(self):
        return '{}: {}'.format(self.instrument.name, self.principle)


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
