# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class SmslibCalls(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    address = models.CharField(max_length=16)
    gateway_id = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'smslib_calls'


class SmslibGateways(models.Model):
    class_field = models.CharField(db_column='class', max_length=64)  # Field renamed because it was a Python reserved word.
    gateway_id = models.CharField(unique=True, max_length=32)
    p0 = models.CharField(max_length=32, blank=True, null=True)
    p1 = models.CharField(max_length=32, blank=True, null=True)
    p2 = models.CharField(max_length=32, blank=True, null=True)
    p3 = models.CharField(max_length=32, blank=True, null=True)
    p4 = models.CharField(max_length=32, blank=True, null=True)
    p5 = models.CharField(max_length=32, blank=True, null=True)
    sender_address = models.CharField(max_length=16, blank=True, null=True)
    priority = models.IntegerField()
    max_message_parts = models.IntegerField()
    delivery_reports = models.IntegerField()
    profile = models.CharField(max_length=32)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'smslib_gateways'


class SmslibGroupRecipients(models.Model):
    group_id = models.IntegerField()
    address = models.CharField(max_length=16)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'smslib_group_recipients'


class SmslibGroups(models.Model):
    group_name = models.CharField(max_length=32)
    group_description = models.CharField(max_length=100)
    enabled = models.IntegerField()
    profile = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'smslib_groups'


class SmslibIn(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=16)
    encoding = models.CharField(max_length=1)
    text = models.CharField(max_length=4096)
    message_date = models.DateTimeField()
    receive_date = models.DateTimeField()
    gateway_id = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'smslib_in'


class SmslibNumberRoutes(models.Model):
    address_regex = models.CharField(max_length=128)
    gateway_id = models.CharField(max_length=32)
    enabled = models.IntegerField()
    profile = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'smslib_number_routes'


class SmslibOut(models.Model):
    parent_id = models.IntegerField()
    message_id = models.CharField(unique=True, max_length=128)
    create_date = models.DateTimeField()
    sender_address = models.CharField(max_length=16)
    address = models.CharField(max_length=16)
    text = models.CharField(max_length=1024)
    encoding = models.CharField(max_length=1)
    priority = models.IntegerField()
    request_delivery_report = models.IntegerField()
    flash_sms = models.IntegerField()
    sent_status = models.CharField(max_length=1)
    sent_date = models.DateTimeField()
    gateway_id = models.CharField(max_length=32)
    operator_message_id = models.CharField(max_length=128)
    delivery_status = models.CharField(max_length=1)
    delivery_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'smslib_out'
