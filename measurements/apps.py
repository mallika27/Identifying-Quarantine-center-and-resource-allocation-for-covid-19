from django.apps import AppConfig



class MeasurementsConfig(AppConfig):
    name = 'measurements'
    verbose_name = 'Measurement between 2 locations'
class QuarantineConfig(AppConfig):
    name = 'quarantine'
    verbose_name = 'location'
