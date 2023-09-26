from django.contrib import admin
from .models import reactor_unit,unit_report


# Register your models here.
admin.site.register(reactor_unit)
admin.site.register(unit_report)
