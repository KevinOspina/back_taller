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


admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Principle, PrincipleAdmin)
