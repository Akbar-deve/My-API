from django.urls import include,path
from rest_framework import routers
from doctorapp.views import DocotorView,PatientViewSet

router = routers.DefaultRouter()

router.register(r'patient',PatientViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('doctor/',DocotorView.as_view()),

]