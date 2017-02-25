# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 09:26
from __future__ import unicode_literals

import dirtyfields.dirtyfields
from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import idm_core.identity.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('name', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('primary_email', models.EmailField(blank=True, max_length=254)),
                ('id', models.UUIDField(default=idm_core.identity.models.get_uuid, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=1024)),
                ('qualified_label', models.CharField(blank=True, max_length=1024)),
                ('sort_label', models.CharField(blank=True, max_length=1024)),
                ('primary_username', models.CharField(blank=True, max_length=32)),
                ('state', django_fsm.FSMField(choices=[('established', 'established'), ('active', 'active'), ('archived', 'archived'), ('suspended', 'suspended'), ('merged', 'merged')], default='established', max_length=50)),
                ('sex', models.CharField(choices=[('0', 'not known'), ('1', 'male'), ('2', 'female'), ('9', 'not applicable')], default='0', max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('deceased', models.BooleanField(default=False)),
                ('merged_into', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merged_from', to='person.Person')),
                ('primary_name', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_name_of', to='name.Name')),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
