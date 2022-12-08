from django.urls import include,path
from rest_framework import routers
from doctorapp.views import DocotorViewSet,PatientViewSet

router = routers.DefaultRouter()
router.register(r'doctor',DocotorViewSet)
router.register(r'patient',PatientViewSet)
urlpatterns = [
    path('',include(router.urls)),
]