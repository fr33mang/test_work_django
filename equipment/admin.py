
from django.contrib import admin

from equipment.models import Vehicle, VehicleBrand, VehicleModel, VehicleType #, VehicleParam, VehicleParamValue

'''class VehicleParamValuesInline(admin.TabularInline):
    model = VehicleParamValue

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleParamValuesInline]'''

admin.site.register(Vehicle)
admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
#admin.site.register(VehicleParam)
#admin.site.register(VehicleParamValue)
admin.site.register(VehicleType)