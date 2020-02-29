from django.db import models
from enum import Enum

from django_fsm import FSMField, transition
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
"""
                         <------- start -----<----<-   Re Opened
                         |                                 |
                         |                                 |
Open -----start----> In Progress ---->--complete-----> Complete
"""
STATES = ('Open', 'In Progress', 'Complete', 'Re Opened')
STATES = list(zip(STATES, STATES))


class ReportTypeChoice(Enum):  # A subclass of Enum
    Eircode = "Eircode"
    NearbyFacilities = "NearbyFacilities"


class ReportType(models.Model):
    report_type = models.CharField(max_length=100)  # e.g. Eircode

    def __str__(self):
        return self.report_type


class Report(models.Model):
    title = models.CharField(max_length=255, default='Nearby Facilities')
    state = FSMField(default='Open')
    date_submitted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    models.FileField(upload_to='reports')

    @transition(field=state, source=['Open', 'Re Opened'], target='In Progress')
    def start(self):
        """
             This method will contain the action that needs to be taken once the
             state is changed. Such as notifying Users.
             """
        pass

    @transition(field=state, source=['In Progress', 'Re Opened'], target='Complete')
    def complete(self):
        """
             This method will contain the action that needs to be taken once the
             state is changed. S    uch as notifying Users
             """
        pass

    def __str__(self):
        return f"{self.report_type}-{self.title}"


# class BaseReportRequest(models.Model):
#     """
#     Every report request must have at least
#     the user and the actual report attached.
#     """
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     report = models.ForeignKey(Report, on_delete=models.DO_NOTHING, db_constraint=False, blank=True, null=True)


class EircodeReportRequest(models.Model):
    """
    A report based on the eircode of the property
    """
    eircode = models.CharField(max_length=50)
    property_image = models.ImageField(default='property.jpg', upload_to='property_pics')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    report = models.ForeignKey(Report, on_delete=models.DO_NOTHING, db_constraint=False, blank=True, null=True)

    def __str__(self):
        return f"Eircode Request {self.pk}"


class NearbyFacilitiesReportRequest(models.Model):
    """
    Some other report based on nearby facilities
    """
    eircode = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    area_radius_meters = models.IntegerField()
    property_image = models.ImageField(default='property.jpg', upload_to='property_pics')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    report = models.ForeignKey(Report, on_delete=models.DO_NOTHING, db_constraint=False, blank=True, null=True)

    def __str__(self):
        return f"Nearby Facilities Request {self.pk}"
