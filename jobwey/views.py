from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from companies.models import Company, Job
# Create your views here.


class HomeView(TemplateView):
    template_name = "home/index.html"
    queryset = Job
    company = Company

    def get_best_company(self):
        return self.company.objects.all().order_by("?")[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs"] = self.queryset.objects.all().order_by("-createdAt")
        context['best_companies'] = self.get_best_company()
        return context
    
    