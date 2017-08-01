# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from configuration_management_tools.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.admin import actions
from django.db import connection, transaction


# Register your models here.
def generate_campaign_data(modeladmin, request, queryset):
    for instance in queryset:
        if SmslibOut.objects.filter(parent_id=instance.id).count()==0:
            cursor = connection.cursor()
            cursor.execute("insert into smslib_out (parent_id,sender_address,address,text,message_id) select campaign_id_id, '+541150505050',address,text,id from configuration_management_tools_campaign_data where campaign_id_id=" + str(instance.id))
    generate_campaign_data.short_description = "Generate Campaign Data"
        
class CampaignDataResource(resources.ModelResource):
    campaign_id = fields.Field(
        column_name='campaign_id',
        attribute='campaign_id',
        widget=ForeignKeyWidget(Campaign, 'name'))
    
    class Meta:
        model = Campaign_data

class CampaingDataAdmin(ImportExportModelAdmin):
    list_display = ('campaign_id', 'address', 'text')
    ordering = ('address',)
    list_filter = ('campaign_id',)
    search_fields = ('campaign_id',)
    resources_class = CampaignDataResource
    
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'start', 'end', 'is_active')
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'is_active')
    actions = [generate_campaign_data]

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Campaign_data, CampaingDataAdmin)
# admin.site.register(SmslibCalls)
admin.site.register(SmslibGateways)
# admin.site.register(SmslibGroupRecipients)
# admin.site.register(SmslibGroups)
# admin.site.register(SmslibIn)
admin.site.register(SmslibNumberRoutes)

# admin.site.register(SmslibOut)
