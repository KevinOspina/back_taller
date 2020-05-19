from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from meejel.views import *

router = routers.DefaultRouter()

router.register('instrument', InstrumentViewSet, basename='instrument')
router.register('assessment', AssessmentViewSet, basename='assessment')

instrument_router = routers.NestedSimpleRouter(router, 'instrument', lookup='instrument')

assessment_router = routers.NestedSimpleRouter(router, 'assessment', lookup='assessment')
assessment_router.register('principle', PrincipleViewSet, base_name='principles')
assessment_router.register('evidence', EvidenceViewSet, base_name='evidences')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(instrument_router.urls)),
    path('', include(assessment_router.urls)),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
