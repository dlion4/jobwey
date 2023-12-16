from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from .forms import LoginForm, ForgotPasswordForm
from django.views.generic import View, TemplateView, FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import AccountUser
from companies.models import Job, Company
from applicants.models import Application
from testimonials.forms import TestimonyAdminForm, Testimony


class ContextDataMixins:
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class LoginView(ContextDataMixins, TemplateView):
    template_name = "account/auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("jobwey:home")


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.clean_email()
            password = form.clean_password()
            user = authenticate(request, email=email, password=password)
            if user is not None:
                messages.success(request, "Successful login")
                login(request, user)
                return redirect(self.success_url)
            messages.error(request, "Invalid user credentials")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "Thanks for spending sometime in our website. See you soon!")
        return redirect("jobwey:home")
    


class SignUpView(ContextDataMixins, TemplateView):
    template_name = "account/auth/signup.html"
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("jobwey:home")
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.clean_email()
            password = form.clean_password()
            username = form.clean_username()

            user = authenticate(request, email=email, password=password)

            if user:
                messages.warning(request, "User Email already taken!")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            user = AccountUser.objects.create_user(
                email, password, username
            )
            user.agree_to_terms=True
            user.save()
            messages.success(request, "Account created successfully")
            return redirect("account:login")
        
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    

class ForgotPasswordView(ContextDataMixins, TemplateView):
    template_name = "account/auth/forgot.html"
    form_class = ForgotPasswordForm
    trial = 5
    support_email="jobwey"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = AccountUser.objects.filter(email=form.clean_email()).all()
            if user:
                return redirect("account:reset-sent")
            messages.error(request, f"Invalid email address. Kindly contact customercare for assistance! <strong>{self.support_email}</strong>")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class ForgotPasswordResetSentView(TemplateView):
    template_name = "account/auth/reset-sent.html"
    

class UpdateProfileView(TemplateView):
    template_name = "account/update_profile.html"

    def get_profile(self, **kwargs):
        return self.request.user.user_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] =  self.get_profile(**kwargs)
        return context


class ProfileView(TemplateView):
    template_name = "account/profile.html"
    application = Application
    form_class = TestimonyAdminForm
    testimonial = Testimony

    def get_profile(self, **kwargs):
        return self.request.user.user_profile
    
    def get_applied_jobs(self, **kwargs):
        return self.application.objects.filter(profile=self.get_profile(**kwargs)).all().order_by("-timestamp")
    
    def get_testimonial(self, **kwargs):
        try: return Testimony.objects.filter(profile=self.get_profile(**kwargs)).last()
        except: return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] =  self.get_profile(**kwargs)
        context['application'] = self.get_applied_jobs(**kwargs)
        context['t_form'] = self.form_class(instance=self.get_profile(**kwargs), initial={
            "testimony":self.get_testimonial(**kwargs).testimony})
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=self.get_testimonial(**kwargs))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile=self.get_profile(**kwargs)
            instance.profile.save()
            instance.save()
            messages.success(request, "Thanks for submitting a testimonial")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        messages.error(request, f"An error occurred: {form.errors}")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


