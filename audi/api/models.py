from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


UNITS_CHOICES = ((unit, unit) for unit in ['кг', 'шт', 'л'])

class Material(models.Model):
    name = models.CharField(max_length=50,
        unique=True)
    units = models.CharField(max_length=10,
        choices=UNITS_CHOICES,
        null=False)

    def __str__(self):
        return self.name


class JobType(models.Model):
    name = models.CharField(max_length=50,
        unique=True)
    materials = models.ManyToManyField(Material,
        related_name='materials')

    def __str__(self):
        return self.name


AUTO_MODEL_CHOICES = ((model, model) for model in ['Audi 1', 'Audi 2'])

class Job(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    job_type = models.ForeignKey(JobType,
        null=True,
        on_delete=models.SET_NULL)
    inspector = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True,
        related_name='jobs',
        on_delete=models.SET_NULL)
    description = models.TextField()
    auto_model = models.CharField(max_length=100,
        null=False,
        choices=AUTO_MODEL_CHOICES)

    def __str__(self):
        return '{0} ({1}) {2}'.format(self.job_type,
            self.created, self.inspector.username)

    def get_required_materials(self):
        return list(map(str, self.job_type.materials.all()))

    def get_reserved_materials(self):
        reserved_items = self.used_materials.all()
        return [item.material.name for item in reserved_items]


class UsedMaterial(models.Model):
    material = models.ForeignKey(Material,
        on_delete=models.CASCADE)
    count = models.FloatField(default=0)
    job = models.ForeignKey(Job,
        related_name='used_materials',
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return '{0}, {1} {2}.'.format(self.material.name,
            self.count, self.material.units)

    def clean(self):
        required_materials = self.job.get_required_materials()
        reserved_materials = self.job.get_reserved_materials()
        name = self.material.name
        if name not in required_materials:
            raise ValidationError(_("That material doesn't required for the job type"))
        if name in reserved_materials:
            raise ValidationError(_("That material is already reserved for the job"))
        super().clean()