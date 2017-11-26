from django.conf import settings
from django.utils.translation import ugettext_lazy as _
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

    def validate(self, data):
        required_materials = data['job'].get_required_materials()
        reserved_materials = data['job'].get_reserved_materials()
        name = data['material'].name
        print(name)
        if name not in required_materials:
            raise serializers.ValidationError(_("That material doesn't required for the job type"))
        if name in reserved_materials:
            raise serializers.ValidationError(_("That material is already reserved for the job"))
        return super().validate(data)


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