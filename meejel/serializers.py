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
        fields = ('name', )


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name', 'owner')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        # response['components'] = ComponentSerializer(instance.components, many=True).data
        response['owner'] = instance.owner.get_full_name()
        response['Objetivos'] = GoalSerializer(Component.objects.filter(instrument=instance, component_type='Objetivos'),
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


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id', 'instrument', 'principles')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['owner'] = instance.instrument.owner.get_full_name()
        response['instrument'] = instance.instrument.name
        response['principles'] = PrincipleSerializer(instance.principles, many=True).data
        return response


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ('id', 'principle', 'grade', 'justification')


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Oname'] = instance.description
        return response


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Rname'] = instance.description
        return response


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Roname'] = instance.description
        return response


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Sname'] = instance.description
        return response


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Maname'] = instance.description
        return response


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('id', 'principle', 'component')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        principle = Principle.objects.get(pk=response['principle'])
        component = Component.objects.get(pk=response['component'])
        response['principle'] = PrincipleSerializer(principle).data
        return response
