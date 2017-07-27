# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from configuration_management_tools.models import *

# Register your models here.
admin.site.register(SmslibCalls)
admin.site.register(SmslibGateways)
admin.site.register(SmslibGroupRecipients)
admin.site.register(SmslibGroups)
admin.site.register(SmslibIn)
admin.site.register(SmslibNumberRoutes)
admin.site.register(SmslibOut)
