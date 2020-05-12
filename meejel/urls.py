from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_jwt.views import obtain_jwt_token

from meejel.views import *

router = routers.DefaultRouter()

router.register('assessment', AssessmentViewSet, basename='assessment')
assessment_router = routers.NestedSimpleRouter(router, 'assessment', lookup='assessment')
assessment_router.register('principle', PrincipleViewSet, base_name='principles')
assessment_router.register('component', ComponentViewSet, base_name='components')

principle_router = routers.NestedSimpleRouter(assessment_router, 'principle', lookup='principle')
principle_router.register('evidence', EvidenceViewSet, base_name='evidences')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(assessment_router.urls)),
    path('', include(principle_router.urls)),
    path('api-token-auth/', obtain_jwt_token),
]
