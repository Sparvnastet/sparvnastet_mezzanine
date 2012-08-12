from apps.sitemanager.models import PuffText, LinkRoll
from django.contrib import admin

class LinkRollAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'published', )
admin.site.register(PuffText)
admin.site.register(LinkRoll, LinkRollAdmin)