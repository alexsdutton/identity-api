# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-14 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('identity_id', models.UUIDField()),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('state', django_fsm.FSMField(choices=[('proposed', 'proposed'), ('approved', 'approved'), ('rejected', 'rejected'), ('previous', 'previous')], default='proposed', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ImageContext',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('subject_to_approval', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.ImageContext'),
        ),
        migrations.AddField(
            model_name='image',
            name='identity_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('identity_id', 'context')]),
        ),
    ]