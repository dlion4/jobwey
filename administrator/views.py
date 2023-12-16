from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from companies.models import Company, Job
from companies.forms import CompanyCreateForm, JobCreateForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify

# Create your views here.

class CreationMixin(TemplateView):
    form_class = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context


class CreateCompanyView(CreationMixin):
    template_name = "company/company_create.html"
    form_class = CompanyCreateForm

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.slug = slugify(form.cleaned_data.get('name'))
            instance.save()
            messages.success(request, f"Successfully created a company {form.cleaned_data.get('name')}")
            return redirect(instance)
        messages.error(request, str(form.errors))
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class UpdateCompanyView(CreationMixin):
    template_name = "company/company_update.html"
    form_class = CompanyCreateForm
    company = Company

    def get_company(self, **kwargs):
        return get_object_or_404(self.company, slug=kwargs.get("slug"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.get_company(**kwargs))
        context['company'] = self.get_company(**kwargs)
        return context
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES, instance=self.get_company(**kwargs))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save()
            messages.success(self.request, "Comapny update successfully")
            print(form.errors)
            return redirect(self.get_company(**kwargs))
        messages.error(self.request, str(form.errors))
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))


class CreateCompanyPositionView(CreationMixin):
    template_name = "company/job/create.html"
    form_class = JobCreateForm
    company = Company

    def get_company(self, **kwargs):
        return self.company.objects.get(slug=kwargs.get("slug"))
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['company'] = self.get_company(**kwargs)
        print(self.get_company(**kwargs))
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = self.get_company(**kwargs)
            instance.company.save()
            instance.slug = slugify(form.cleaned_data.get("title"))
            instance.save()
            messages.success(request, f"Succesfully created a possition for {self.get_company(**kwargs).name}")
            return redirect(instance)
        messages.error(request, f"{form.errors}")
        print(form.errors)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    


    