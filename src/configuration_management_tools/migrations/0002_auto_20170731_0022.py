# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 00:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration_management_tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smslibgateways',
            options={'managed': False, 'verbose_name': 'Gateways'},
        ),
        migrations.AlterModelOptions(
            name='smslibnumberroutes',
            options={'managed': False, 'verbose_name': 'Routes'},
        ),
    ]
