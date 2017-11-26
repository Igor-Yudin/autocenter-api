from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(r'jobtypes', views.JobTypeViewSet)
router.register(r'materials', views.MaterialViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'used_materials', views.UsedMaterialViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]