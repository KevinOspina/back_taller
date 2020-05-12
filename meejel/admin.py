from django.contrib import admin, messages
from .models import *

admin.site.site_header = 'Meejel Administration'
admin.site.index_title = 'MEEJEL'
admin.site.site_title = 'Meejel Admin'


class AssessmentAdmin(admin.ModelAdmin):
    model = Assessment
    list_display = ('name', 'owner')
    list_filter = ('name', 'owner')


class PrincipleAdmin(admin.ModelAdmin):
    model = Principle
    list_display = ('principle', 'grade', 'justification')
    list_filter = ('principle', 'grade')


class ComponentAdmin(admin.ModelAdmin):
    model = Component
    list_display = ('assessment', 'description', 'component_type')
    list_filter = ('assessment', )


class EvidenceAdmin(admin.ModelAdmin):
    model = Evidence
    list_display = ('principle', 'component')


admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Principle, PrincipleAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Evidence, EvidenceAdmin)
