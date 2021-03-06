# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub_be_app', '0002_propsales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singfamhouse',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False, verbose_name=12)),
                ('mean_sfno', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('tot_sfno', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
                ('num_sfno', models.DecimalField(decimal_places=0, max_digits=3, null=True)),
                ('mean_sfoo', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('tot_sfoo', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
                ('num_sfoo', models.DecimalField(decimal_places=0, max_digits=3, null=True)),
                ('prc_sfno', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Health',
        ),
    ]
