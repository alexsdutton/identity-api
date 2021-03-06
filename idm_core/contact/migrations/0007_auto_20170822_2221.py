# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20170703_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'email address', 'verbose_name_plural': 'email addresses'},
        ),
        migrations.AlterModelOptions(
            name='telephone',
            options={'verbose_name': 'telephone number'},
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='email',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='telephone',
            unique_together=set([]),
        ),
    ]
