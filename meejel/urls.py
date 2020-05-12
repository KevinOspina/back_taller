from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_jwt.views import obtain_jwt_token

from meejel.views import *

router = routers.DefaultRouter()

router.register('assessment', AssessmentViewSet, basename='assessment')
assessment_router = routers.NestedDefaultRouter(router, 'assessment', lookup='assessment')
assessment_router.register('principle', PrincipleViewSet, base_name='principles')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(assessment_router.urls)),
    path('api-token-auth/', obtain_jwt_token),
]
