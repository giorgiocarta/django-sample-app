from django.contrib import admin
from .models import (
    ReportType,
    Report,
    EircodeReportRequest,
    NearbyFacilitiesReportRequest
)

# Register your models here.

admin.site.register(ReportType)
admin.site.register(Report)
admin.site.register(EircodeReportRequest)
admin.site.register(NearbyFacilitiesReportRequest)
