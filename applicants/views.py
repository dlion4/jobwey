from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView, TemplateView
from testimonials.models import Testimony
from .models import Application
from companies.models import Job
from .forms import ApplicationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from account.models import Profile
# Create your views here.

class CandidatesListView(ListView):
    template_name = "company/candidates.html"
    context_object_name = "candidates"
    paginate_by = 20
    page_kwarg = "page"
    queryset = Application.objects.all()




class ApplicationCreateView(TemplateView):
    form_class = ApplicationForm
    template_name = "company/job/application.html"
    queryset = Job

    def get_job_object(self, **kwargs):
        return self.queryset.objects.filter(
            company__slug=kwargs.get("company_slug"), 
            slug=kwargs.get("job_slug")).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] =  self.get_job_object(**kwargs)
        context['form'] = self.form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        job = self.get_job_object(**kwargs)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.job = job
            instance.profile = self.request.user.user_profile
            instance.job.positions -= 1
            instance.job.save()
            instance.save()
            form.save()
            messages.success(request, "Your application was submitted successfully.")
            return redirect("jobwey:home")
        messages.error(request, "Error submitting the form. Kindly retry again")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))




class PublicCandidateProfileView(TemplateView):
    template_name = "company/job/public_profile.html"
    profile = Profile
    application = Application
    testimony = Testimony

    def get_testimony(self, **kwargs):
        try: return get_object_or_404(self.testimony, profile=self.get_profile(**kwargs))
        except: return None
    
    def get_profile(self, **kwargs):
        return self.profile.objects.get(pk=kwargs.get("applicant_public_profile_pk"))
    
    def get_latest_application_details(self, **kwargs):
        return self.application.objects.filter(profile=self.get_profile(**kwargs), is_active=True).latest()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] =  self.get_profile(**kwargs)
        context['latest_application_data'] = self.get_latest_application_details(**kwargs)
        context['testimony'] = self.get_testimony(**kwargs)
        return context

    