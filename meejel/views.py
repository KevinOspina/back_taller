import logging
import copy

from django.db.utils import IntegrityError
from rest_framework import pagination, status
from rest_framework import viewsets
from rest_framework.response import *

from meejel.serializers import *

log = logging.getLogger("gunicorn")


class PaginationStandard(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 25
    page_size_query_param = 'page_size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data,
            'total_pages': self.page.paginator.num_pages
        })


class InstrumentViewSet(viewsets.ModelViewSet):
    serializer_class = InstrumentSerializer
    # pagination_class = PaginationStandard

    def get_queryset(self):
        return self.request.user.instruments.all()

    def create(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response({'error': 'you are not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            name = request.data['name']
            goals = request.data['Objetivos']
            rules = request.data['Reglas']
            roles = request.data['Roles']
            steps = request.data['Pasos']
            materials = request.data['Materiales']
        except KeyError:
            return Response({'error': 'missing fields'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            new_instrument = Instrument.objects.create(name=name, owner=self.request.user)
            for i in goals:
                Component.objects.create(component_type='Objetivos', description=i['Oname'], instrument=new_instrument)
            for i in rules:
                Component.objects.create(component_type='Reglas', description=i['Rname'], instrument=new_instrument)
            for i in roles:
                Component.objects.create(component_type='Roles', description=i['Roname'], instrument=new_instrument)
            for i in steps:
                Component.objects.create(component_type='Pasos', description=i['Sname'], instrument=new_instrument)
            for i in materials:
                Component.objects.create(component_type='Materiales', description=i['Maname'], instrument=new_instrument)
            return Response({'ok': 'created'}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'an instrument with that name already exists'}, status=status.HTTP_409_CONFLICT)


class AssessmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer
    # pagination_class = PaginationStandard

    def get_queryset(self):
        return Assessment.objects.filter(instrument__owner=self.request.user)


class PrincipleViewSet(viewsets.ModelViewSet):
    serializer_class = PrincipleSerializer

    def get_queryset(self):
        assessment_id = self.kwargs['assessment_pk']
        queryset = Principle.objects.filter(assessment_id=assessment_id)
        return queryset

    def create(self, request, *args, **kwargs):
        assessment_id = self.kwargs['assessment_pk']
        new_principle = Principle.objects.create(principle=request.data['principle'], grade=request.data['grade'],
                                                 justification=request.data['justification'], assessment_id=assessment_id)
        return Response(self.serializer_class(new_principle).data, status=status.HTTP_200_OK)


class EvidenceViewSet(viewsets.ModelViewSet):
    serializer_class = EvidenceSerializer

    def get_queryset(self):
        assessment = self.kwargs['assessment_pk']
        queryset = Evidence.objects.filter(principle__assessment=assessment)
        return queryset
