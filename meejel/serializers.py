from distutils.command.install import install

from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name', 'level')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['owner'] = instance.owner.get_full_name()
        response['Objetivos'] = GoalSerializer(
            Component.objects.filter(instrument=instance, component_type='Objetivos'),
            many=True).data
        response['Reglas'] = RuleSerializer(
            Component.objects.filter(instrument=instance, component_type='Reglas'),
            many=True).data
        response['Roles'] = RoleSerializer(
            Component.objects.filter(instrument=instance, component_type='Roles'),
            many=True).data
        response['Pasos'] = StepSerializer(
            Component.objects.filter(instrument=instance, component_type='Pasos'),
            many=True).data
        response['Materiales'] = MaterialSerializer(
            Component.objects.filter(instrument=instance, component_type='Materiales'),
            many=True).data
        return response


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Oname'] = instance.description
        return response


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Rname'] = instance.description
        return response


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Roname'] = instance.description
        return response


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Sname'] = instance.description
        return response


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Maname'] = instance.description
        return response


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('id', 'principle',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        principle = Principle.objects.get(pk=response['principle'])
        response['principle'] = PrincipleSerializer(principle).data
        return response


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('description', 'component_type')


class EvidencePrincipleSerializer(serializers.ModelSerializer):
    component = ComponentSerializer()

    class Meta:
        model = Evidence
        fields = ('id', 'component')


class PrincipleSerializer(serializers.ModelSerializer):
    evidences = EvidencePrincipleSerializer(many=True)

    class Meta:
        model = Principle
        fields = ('id', 'principle', 'grade', 'weight', 'evidences')
