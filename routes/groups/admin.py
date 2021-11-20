from django.contrib import admin
from .models import *


class GroupAdmin(admin.ModelAdmin):
    fields = ["number", "uuid"]
    readonly_fields = ["uuid"]


admin.site.register(Group, GroupAdmin)
admin.site.register(Membership)
