from django.contrib import admin
from .models import reactor_unit,unit_report,fact_table


# Register your models here.
admin.site.register(reactor_unit)
admin.site.register(unit_report)
admin.site.register(fact_table)
