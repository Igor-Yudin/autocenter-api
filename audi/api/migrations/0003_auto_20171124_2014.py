# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 17:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20171124_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('auto_model', models.CharField(choices=[('Audi 1', 'Audi 1'), ('Audi 2', 'Audi 2')], max_length=100)),
                ('inspector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsedMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Material')),
            ],
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='materials',
            field=models.ManyToManyField(related_name='materials', to='api.Material'),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.JobType'),
        ),
        migrations.AddField(
            model_name='job',
            name='used_materials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='used_materials', to='api.UsedMaterial'),
        ),
    ]