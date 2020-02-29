from django.shortcuts import render

# Create your views here.
from .models import Report, EircodeReportRequest, NearbyFacilitiesReportRequest
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ReportsListView(ListView):
    """
    List view with pagination
    """
    model = Report
    template_name = 'reports/home.html'  # <app> / <model>_<viewtype>.html

    context_object_name = 'reports'
    ordering = ['-date_submitted', 'title']
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['picture'] = Picture.objects.filter(your_condition)
    #     for item in context['reports']:
    #         # print(type(item))
    #         # print(type(item.eircodereportrequest_set.all().first()))
    #         # print(type(item.nearbyfacilitiesreportrequest_set.all().first()))
    #
    #         print(dir(item.report_type))
    #         # print(item.report_type)
    #         # print(item.eircodereportrequest_set.all().first())
    #         # print(item.nearbyfacilitiesreportrequest_set.all().first())
    #         # print(item.state[0])
    #     return context
