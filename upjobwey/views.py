from django.views.generic import TemplateView


class RoboticView(TemplateView):
    template_name = "robots.txt"

class AboutUsView(TemplateView):
    template_name = "aboutus.html"

class ContractView(TemplateView):
     template_name = "contract.html"

class PrivacyView(TemplateView):
     template_name = "privacy.html"

class TermsView(TemplateView):
    template_name = "terms.html"

class ContactView(TemplateView):
    template_name = "contactus.html"
