# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-11 21:15
from __future__ import unicode_literals

import dirtyfields.dirtyfields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attested_by', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(), blank=True,
                                                                          default=[], size=None)),
                ('identity_id', models.UUIDField()),
                ('validated', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('identity_content_type', 'identity_id', 'order'),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ContactContext',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attested_by', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(), blank=True, default=[], size=None)),
                ('identity_id', models.UUIDField()),
                ('validated', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField()),
                ('value', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('identity_content_type', 'identity_id', 'order'),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OnlineAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attested_by', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(),
                                                                          blank=True, default=[], size=None)),
                ('identity_id', models.UUIDField()),
                ('validated', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('identity_content_type', 'identity_id', 'order'),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attested_by', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(), blank=True, default=[], size=None)),
                ('identity_id', models.UUIDField()),
                ('validated', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField()),
                ('value', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('identity_content_type', 'identity_id', 'order'),
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
