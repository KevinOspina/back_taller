from django.db import models
from django.contrib.auth.models import User, Group
from .extras import GRADE_CHOICES, PRINCIPLE_CHOICES, EVIDENCE_CHOICES


class Assessment(models.Model):
    """
    An assessment related to an specific user
    """
    name = models.CharField(null=False, max_length=100)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assessments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"
        unique_together = ("name", "owner")


class Principle(models.Model):
    """
    Principle composing an assessment
    """
    principle = models.CharField(max_length=30, null=False, choices=PRINCIPLE_CHOICES)
    grade = models.CharField(max_length=30, null=False, choices=GRADE_CHOICES)
    justification = models.CharField(max_length=150, null=False)
    assessment = models.ForeignKey(Assessment, on_delete=models.PROTECT, related_name='principles')

    class Meta:
        verbose_name = "Principio"
        verbose_name_plural = "Principios"
        unique_together = ("assessment", "principle")

    def __str__(self):
        return '{}: {}'.format(self.principle, self.justification)


class Component(models.Model):
    description = models.TextField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='components')
    component_type = models.CharField(max_length=20, choices=EVIDENCE_CHOICES)

    def __str__(self):
        return '{}: {}'.format(self.component_type, self.description)

    class Meta:
        verbose_name = "Component"
        verbose_name_plural = "Componentes"


class Evidence(models.Model):
    """
    Represents all the evidence of a principle on an strategy
    """
    principle = models.ForeignKey(Principle, on_delete=models.PROTECT, related_name='evidences')
    component = models.ForeignKey(Component, on_delete=models.PROTECT)

    def __str__(self):
        return '{}: {}'.format(self.principle.principle, self.component.description)
