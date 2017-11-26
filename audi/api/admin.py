from django.contrib import admin

from api.models import Material
from api.models import JobType
from api.models import UsedMaterial
from api.models import Job


class UsedMaterialAdmin(admin.ModelAdmin):
    list_display = ('material',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)


class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Material, MaterialAdmin)
admin.site.register(JobType, JobTypeAdmin)
admin.site.register(UsedMaterial, UsedMaterialAdmin)
admin.site.register(Job)