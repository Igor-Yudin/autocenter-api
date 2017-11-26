from django.conf import settings
from rest_framework import serializers

from api.models import JobType
from api.models import Material
from api.models import UsedMaterial
from api.models import Job


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True,
        read_only=True)
    class Meta:
        model = JobType
        fields = '__all__'


class UsedMaterialSerializer(serializers.ModelSerializer):
    material = serializers.SlugRelatedField(read_only=False,
        queryset=Material.objects.all(),
        slug_field='name')
    class Meta:
        model = UsedMaterial
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    used_materials = UsedMaterialSerializer(many=True,
        read_only=True)
    job_type = serializers.SlugRelatedField(read_only=False,
        queryset=JobType.objects.all(),
        slug_field='name')
    inspector = serializers.ReadOnlyField(source='inspector.username')
    class Meta:
        model = Job
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = '__all__'