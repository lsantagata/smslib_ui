# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmslibCalls',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(max_length=16)),
                ('gateway_id', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'smslib_calls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmslibGateways',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_field', models.CharField(db_column='class', max_length=64)),
                ('gateway_id', models.CharField(max_length=32, unique=True)),
                ('p0', models.CharField(blank=True, max_length=32, null=True)),
                ('p1', models.CharField(blank=True, max_length=32, null=True)),
                ('p2', models.CharField(blank=True, max_length=32, null=True)),
                ('p3', models.CharField(blank=True, max_length=32, null=True)),
                ('p4', models.CharField(blank=True, max_length=32, null=True)),
                ('p5', models.CharField(blank=True, max_length=32, null=True)),
                ('sender_address', models.CharField(blank=True, max_length=16, null=True)),
                ('priority', models.IntegerField()),
                ('max_message_parts', models.IntegerField()),
                ('delivery_reports', models.IntegerField()),
                ('profile', models.CharField(max_length=32)),
                ('enabled', models.IntegerField()),
            ],
            options={
                'db_table': 'smslib_gateways',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmslibGroupRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('address', models.CharField(max_length=16)),
                ('enabled', models.IntegerField()),
            ],
            options={
                'db_table': 'smslib_group_recipients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmslibGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=32)),
                ('group_description', models.CharField(max_length=100)),
                ('enabled', models.IntegerField()),
                ('profile', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'smslib_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmslibIn',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=16)),
                ('encoding', models.CharField(max_length=1)),
                ('text', models.CharField(max_length=4096)),
                ('message_date', models.DateTimeField()),
                ('receive_date', models.DateTimeField()),
                ('gateway_id', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'smslib_in',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmslibNumberRoutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_regex', models.CharField(max_length=128)),
                ('gateway_id', models.CharField(max_length=32)),
                ('enabled', models.IntegerField()),
                ('profile', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'smslib_number_routes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmslibOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField()),
                ('message_id', models.CharField(max_length=128, unique=True)),
                ('create_date', models.DateTimeField()),
                ('sender_address', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=16)),
                ('text', models.CharField(max_length=1024)),
                ('encoding', models.CharField(max_length=1)),
                ('priority', models.IntegerField()),
                ('request_delivery_report', models.IntegerField()),
                ('flash_sms', models.IntegerField()),
                ('sent_status', models.CharField(max_length=1)),
                ('sent_date', models.DateTimeField()),
                ('gateway_id', models.CharField(max_length=32)),
                ('operator_message_id', models.CharField(max_length=128)),
                ('delivery_status', models.CharField(max_length=1)),
                ('delivery_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'smslib_out',
                'managed': False,
            },
        ),
    ]