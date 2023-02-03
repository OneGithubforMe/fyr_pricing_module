from django.contrib import admin
from .models import *

# Register your models here.
class DistanceBasePricingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DistanceBasePricing._meta.get_fields()]

admin.site.register(DistanceBasePricing, DistanceBasePricingAdmin)


class TimeMultiplierFactorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TimeMultiplierFactor._meta.get_fields()]
admin.site.register(TimeMultiplierFactor, TimeMultiplierFactorAdmin)



class DistanceAdditionalPriceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DistanceAdditionalPrice._meta.get_fields()]
admin.site.register(DistanceAdditionalPrice, DistanceAdditionalPriceAdmin)

