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


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('name', 'owner', 'principles')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['principles'] = PrincipleSerializer(instance.principles, many=True).data
        response['components'] = ComponentSerializer(instance.components, many=True).data
        return response


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ('principle', 'grade', 'justification')


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('description', 'component_type')


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('principle', 'component')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        principle = Principle.objects.get(pk=response['principle'])
        component = Component.objects.get(pk=response['component'])
        response['principle'] = PrincipleSerializer(principle).data
        response['component'] = ComponentSerializer(component).data
        return response
