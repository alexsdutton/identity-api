# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-20 19:21
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20170816_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecontext',
            old_name='subject_to_approval',
            new_name='subject_to_acceptance',
        ),
        migrations.AlterField(
            model_name='image',
            name='state',
            field=django_fsm.FSMField(choices=[('proposed', 'proposed'), ('accepted', 'accepted'), ('rejected', 'rejected'), ('previous', 'previous')], default='proposed', max_length=50),
        ),
    ]
