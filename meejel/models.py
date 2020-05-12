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
        return '{} {}'.format(self.principle, self.justification)


class Evidence(models.Model):
    """
    Represents all the evidence of a principle on an strategy
    """
    sort_of = models.CharField(max_length=30, null=False, choices=EVIDENCE_CHOICES)
    description = models.CharField(null=False, max_length=150)
    principle = models.ForeignKey(Principle, on_delete=models.PROTECT, related_name='evidences')

    def __str__(self):
        return self.description


class Rule(models.Model):
    description = models.CharField(max_length=100)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='rules')
    evidence_of = models.OneToOneField(Evidence, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Regla"
        verbose_name_plural = "Reglas"


class Material(models.Model):
    description = models.CharField(max_length=100)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='materials')
    evidence_of = models.OneToOneField(Evidence, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"


class Goal(models.Model):
    description = models.CharField(max_length=100)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='goals')
    evidence_of = models.OneToOneField(Evidence, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Objetivo"
        verbose_name_plural = "Objetivos"


class Role(models.Model):
    description = models.CharField(max_length=100)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='roles')
    evidence_of = models.OneToOneField(Evidence, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"


class Step(models.Model):
    description = models.CharField(max_length=100)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='steps')
    evidence_of = models.OneToOneField(Evidence, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Paso"
        verbose_name_plural = "Pasos"
