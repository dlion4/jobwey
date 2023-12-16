from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View, DetailView, ListView
from .models import Company, Job
# Create your views here.

class CompanyListView(ListView):
    template_name = "company/companies.html"
    context_object_name = "companies"
    paginate_by = 20
    page_kwarg = "page"
    queryset = Company.objects.all()


    


class CompanyDetailView(DetailView):
    queryset = Company.objects.all()
    template_name = "company/company.html"
    slug_field = "slug"
    context_object_name = "company"


class JobListView(ListView):
    template_name = "company/job/jobs.html"
    context_object_name = "jobs"
    queryset = Job.objects.all()
    paginate_by = 10
    page_kwarg = "page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.queryset.order_by("-createdAt")
        return context
    
class JobDetailView(TemplateView):
    queryset = Job.objects.all()
    model = Job
    template_name = "company/job/job.html"
    context_object_name = "job"

    def get_object(self, **kwargs):
        job = self.model.objects.filter(company__slug=kwargs.get("company_slug"), slug=kwargs.get("job_slug")).first()
        return job
    
    def get_related_jobs(self, **kwargs):
        try:
            return self.model.objects.filter(company__slug=kwargs.get("company_slug"), positions__gte=1).all().exclude(slug=self.get_object(**kwargs).slug, company__slug=self.get_object(**kwargs).company.slug).order_by("?")
        except:
            return None
        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context[self.context_object_name] = self.get_object(**kwargs)
        context['related_jobs'] = self.get_related_jobs(**kwargs)
        return context
    
    
        

