from django.views.generic import TemplateView


class RoboticView(TemplateView):
    template_name = "robots.txt"