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
        return response


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ('principle', 'grade', 'justification')


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'
