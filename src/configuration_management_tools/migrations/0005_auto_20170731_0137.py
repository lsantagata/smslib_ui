# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 01:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration_management_tools', '0004_campaign_campaign_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign_data',
            options={'verbose_name': 'Campaign Data'},
        ),
    ]
