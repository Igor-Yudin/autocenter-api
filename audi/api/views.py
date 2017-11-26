from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from api.models import JobType
from api.models import Material
from api.models import UsedMaterial
from api.models import Job

from api.serializers import JobTypeSerializer
from api.serializers import MaterialSerializer
from api.serializers import UsedMaterialSerializer
from api.serializers import JobSerializer

from api.permissions import *


class JobTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UsedMaterialViewSet(viewsets.ModelViewSet):
    queryset = UsedMaterial.objects.all()
    serializer_class = UsedMaterialSerializer
    permission_classes = (permissions.IsAuthenticated,)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(inspector=self.request.user)