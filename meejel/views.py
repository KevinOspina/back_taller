import logging
import copy

from django.db.utils import IntegrityError
from rest_framework import pagination, status
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
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


@api_view(['POST'])
@permission_classes([])
def sign(request, *args, **kwargs):
    try:
        username = request.data['username']
        password = request.data['password']
        User.objects.create(username=username, password=password)
        return Response({"error": "Success"}, status=status.HTTP_200_OK)
    except KeyError:
        return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)


class InstrumentViewSet(viewsets.ModelViewSet):
    serializer_class = InstrumentSerializer
    # pagination_class = PaginationStandard

    def get_queryset(self):
        return self.request.user.instruments.all()

    def destroy(self: Instrument, request, *args, **kwargs):
        self.principles.all().delete()
        return Response({'error': 'Principios borrados'}, status=status.HTTP_400_BAD_REQUEST)

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


class PrincipleViewSet(viewsets.ModelViewSet):
    serializer_class = PrincipleSerializer

    def get_queryset(self):
        instrument_id = self.kwargs['instrument_pk']
        queryset = Principle.objects.filter(instrument_id=instrument_id)
        return queryset

    def create(self, request, *args, **kwargs):
        instrument_id = self.kwargs['instrument_pk']
        new_principle = Principle.objects.create(principle=request.data['principle'], grade=request.data['grade'],
                                                 instrument_id=instrument_id)
        return Response(self.serializer_class(new_principle).data, status=status.HTTP_200_OK)


class EvidenceViewSet(viewsets.ModelViewSet):
    serializer_class = EvidenceSerializer

    def get_queryset(self):
        instrument = self.kwargs['instrument_pk']
        queryset = Evidence.objects.filter(principle__instrument=instrument)
        return queryset

    def create(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response({'error': 'you are not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            instrument = Instrument.objects.get(pk=request.data['instrument_id'])
            principles = request.data['Principios']
        except KeyError:
            return Response({'error': 'missing fields'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            for i in principles:
                principle = i['id']
                evidences = i['evidencias']
                level = i['nivel']
                new_principle = Principle.objects.create(instrument=instrument, grade=level, principle=principle)
                for j in evidences:
                    component = Component.objects.get(pk=j)
                    Evidence.objects.create(principle=new_principle, component=component)
            return Response({'ok': 'created'}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'an instrument with that name already exists'}, status=status.HTTP_409_CONFLICT)
