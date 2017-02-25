# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 09:26
from __future__ import unicode_literals

import dirtyfields.dirtyfields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('alpha_2', models.CharField(db_index=True, max_length=2, null=True, unique=True)),
                ('alpha_3', models.CharField(db_index=True, max_length=3, null=True, unique=True)),
                ('numeric', models.CharField(db_index=True, max_length=3, null=True, unique=True)),
            ],
            options={
                'ordering': ('label',),
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attested_by', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(), default=[], size=None)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nationality.Country')),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='country',
            name='people',
            field=models.ManyToManyField(related_name='nationalities', through='nationality.Nationality', to='person.Person'),
        ),
    ]
