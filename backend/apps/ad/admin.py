from django.contrib import admin

from apps.ad.models.ad_compliance import ADCompliance
from apps.ad.models.airworthiness_directive import AirworthinessDirective
from apps.ad.models.applicability_rule import ADApplicabilityRule

admin.site.register(ADCompliance)
admin.site.register(AirworthinessDirective)
admin.site.register(ADApplicabilityRule)
