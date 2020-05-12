import logging

from rest_framework import pagination
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


class AssessmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        return self.request.user.assessments.all()


class PrincipleViewSet(viewsets.ModelViewSet):
    serializer_class = PrincipleSerializer

    def get_queryset(self):
        assessment_id = self.kwargs['assessment_pk']
        queryset = Principle.objects.filter(assessment_id=assessment_id)
        return queryset


class ComponentViewSet(viewsets.ModelViewSet):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        assessment_id = self.kwargs['assessment_pk']
        queryset = Component.objects.filter(assessment_id=assessment_id)
        return queryset


class EvidenceViewSet(viewsets.ModelViewSet):
    serializer_class = EvidenceSerializer

    def get_queryset(self):
        print(self.kwargs)
        principle_id = self.kwargs['principle_pk']
        queryset = Evidence.objects.filter(principle_id=principle_id)
        return queryset
