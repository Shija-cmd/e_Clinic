from django.contrib import admin
from .models import Patient
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

# For exporting and importing patients data
class PatientInfo(resources.ModelResource):

    class Meta:
        model = Patient
        
class PatientAdmin(ImportExportModelAdmin):
    resource_classes = [PatientInfo]
# Registering the models in the admin pannel
admin.site.register(Patient, PatientAdmin)