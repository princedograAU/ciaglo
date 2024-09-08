from django.contrib import admin

from agency import models


@admin.register(models.Agency)
class AgencyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Agent)
class AgentAdmin(admin.ModelAdmin):
    pass
