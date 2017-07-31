# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from configuration_management_tools.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.db import connection, transaction
from django.dispatch import receiver 
from import_export.signals import post_import

# Register your models here.


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

@receiver(post_import, dispatch_uid='camp_data') 
def post_import_handler(sender, **kwargs):
    cursor = connection.cursor()
    cursor.execute("insert into smslib_out (parent_id,sender_address,address,text) select campaign_id_id, '+541150505050',address,text from configuration_management_tools_campaign_data where campaign_id_id=" + str(last_id_camp))
    transaction.commit()
        
           
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Campaign_data, CampaingDataAdmin)
# admin.site.register(SmslibCalls)
admin.site.register(SmslibGateways)
# admin.site.register(SmslibGroupRecipients)
# admin.site.register(SmslibGroups)
# admin.site.register(SmslibIn)
admin.site.register(SmslibNumberRoutes)

# admin.site.register(SmslibOut)
