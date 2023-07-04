from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from measurements.resources import Quarantine_Resource,city_Resource

# Register your models here.
class QuarantineAdmin(ImportExportModelAdmin):
    resource_class = Quarantine_Resource
class cityAdmin(ImportExportModelAdmin):
    list_display = ("rank", "city","Place")
    resource_class = city_Resource

admin.site.register(Measurement)
admin.site.register(Quarantine, QuarantineAdmin)
admin.site.register(city,cityAdmin)