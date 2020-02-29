from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Report, EircodeReportRequest, ReportType, NearbyFacilitiesReportRequest, ReportTypeChoice


@receiver(post_save, sender=EircodeReportRequest)
def create_eircode_report(sender, instance: EircodeReportRequest, created, **kwargs):
    """

    Create automatically a profile every time a user is created

    :param sender:
    :param instance: the instance of the user
    :param created: if the user was created
    :param kwargs:
    :return:
    """
    report_type = ReportType.objects.filter(report_type=ReportTypeChoice.Eircode.value).first()

    if created:
        report = Report.objects.create(
            report_type=report_type,
            title=instance.eircode
        )
        instance.report = report
        instance.save()


@receiver(post_save, sender=NearbyFacilitiesReportRequest)
def create_nearby_facilities_report(sender, instance: NearbyFacilitiesReportRequest, created, **kwargs):
    """

    Create automatically a profile every time a user is created

    :param sender:
    :param instance: the instance of the user
    :param created: if the user was created
    :param kwargs:
    :return:
    """
    report_type = ReportType.objects.filter(report_type=ReportTypeChoice.NearbyFacilities.value).first()

    print("---------------------------------")
    print("---------------------------------")
    print("---------------------------------")
    print(report_type)
    print("---------------------------------")
    print("---------------------------------")
    print("---------------------------------")

    if created:
        report = Report.objects.create(
            report_type=report_type,
        )
        instance.report = report
        instance.save()
