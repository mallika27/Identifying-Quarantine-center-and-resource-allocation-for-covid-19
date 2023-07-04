from import_export import resources
from measurements.models import Quarantine,city

class Quarantine_Resource(resources.ModelResource):
    class Meta:
        model=Quarantine
class city_Resource(resources.ModelResource):
    class Meta:
        model= city