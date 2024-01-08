from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from companies.models import Company, Job
from .models import Visa, Service
from posts.models import Post

# Create your views here.


class ContextMixin:
    queryset = None
    context_object_name = ""
    order_by = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SingleObjectMixin:
    look_up_field = ""
    context_object_name = ""
    model = None

    def get_object(self, **kwargs):
        return get_object_or_404(self.model, slug=kwargs.get(self.look_up_field))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.get_object(**kwargs)
        return context


class HomeView(TemplateView):
    template_name = "home/index.html"
    queryset = Job
    company = Company
    posts = Post.objects.all()

    def get_best_company(self):
        return self.company.objects.all().order_by("?")[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs"] = self.queryset.objects.all().order_by("-createdAt")
        context["best_companies"] = self.get_best_company()
        context["posts"] = self.posts.order_by("-id")[:3]
        return context


class VisaListView(TemplateView):
    template_name = "jobwey/visas.html"
    queryset = Visa.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["visas"] = self.queryset
        return context


class ServiceListView(TemplateView):
    template_name = "jobwey/services.html"
    queryset = Service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = self.queryset
        return context


class VisaDetailView(SingleObjectMixin, TemplateView):
    template_name = "jobwey/visa.html"
    model = Visa
    look_up_field = "slug"
    context_object_name = "visa"


class ServiceDetailView(SingleObjectMixin, TemplateView):
    template_name = "jobwey/service.html"
    model = Service
    look_up_field = "slug"
    context_object_name = "service"
