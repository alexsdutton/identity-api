# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('identity', '0001_initial'),
        ('relationship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telephone',
            name='affiliation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationship.Affiliation'),
        ),
        migrations.AddField(
            model_name='telephone',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.ContactContext'),
        ),
        migrations.AddField(
            model_name='telephone',
            name='identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identity.Identity'),
        ),
        migrations.AddField(
            model_name='email',
            name='affiliation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationship.Affiliation'),
        ),
        migrations.AddField(
            model_name='email',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.ContactContext'),
        ),
        migrations.AddField(
            model_name='email',
            name='identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='identity.Identity'),
        ),
        migrations.AddField(
            model_name='address',
            name='affiliation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationship.Affiliation'),
        ),
        migrations.AddField(
            model_name='address',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.ContactContext'),
        ),
        migrations.AddField(
            model_name='address',
            name='identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identity.Identity'),
        ),
        migrations.AlterUniqueTogether(
            name='telephone',
            unique_together=set([('identity', 'order')]),
        ),
        migrations.AlterUniqueTogether(
            name='email',
            unique_together=set([('identity', 'order')]),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('identity', 'order')]),
        ),
    ]