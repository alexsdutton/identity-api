# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import idm_core.identity.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('organization', '0001_initial'),
        ('identifier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=idm_core.identity.models.get_uuid, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='IdentityPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_id', models.UUIDField()),
                ('all_organizations', models.BooleanField(default=False)),
                ('all_identifier_types', models.BooleanField(default=False)),
                ('identifier_types', models.ManyToManyField(blank=True, to='identifier.IdentifierType')),
                ('identity_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('organizations', models.ManyToManyField(blank=True, to='organization.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='identity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='identity.Identity'),
        ),
    ]
