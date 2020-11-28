# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-06 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auvsi_suas', '0002_suas2020_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionconfig',
            name='air_drop_boundary_points',
            field=models.ManyToManyField(
                related_name='missionconfig_air_drop_boundary_points',
                to='auvsi_suas.Waypoint'),
        ),
        migrations.AddField(
            model_name='missionconfig',
            name='lost_comms_pos',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='missionconfig_lost_comms_pos',
                to='auvsi_suas.GpsPosition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='missionconfig',
            name='ugv_drive_pos',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='missionconfig_ugv_drive_pos',
                to='auvsi_suas.GpsPosition'),
            preserve_default=False,
        ),
    ]