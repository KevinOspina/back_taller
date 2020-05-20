from django.contrib import admin, messages
from .models import *

admin.site.site_header = 'Meejel Administration'
admin.site.index_title = 'MEEJEL'
admin.site.site_title = 'Meejel Admin'


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    model = Instrument
    list_display = ('name', 'owner')
    list_filter = ('name', 'owner')


@admin.register(Principle)
class PrincipleAdmin(admin.ModelAdmin):
    model = Principle
    list_display = ('principle', 'grade', )
    list_filter = ('principle', 'grade')


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    model = Component
    list_display = ('instrument', 'description', 'component_type')
    list_filter = ('instrument', )


@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    model = Evidence
    list_display = ('principle', 'component')
