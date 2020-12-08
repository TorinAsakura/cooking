from django.contrib import admin

from models import TrackingType, Tracking


class TrackingAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created', 'content_type')

admin.site.register(Tracking, TrackingAdmin)
admin.site.register(TrackingType)