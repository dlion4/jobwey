from django.urls import path
from . import views

app_name = "jobwey"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("visa/", views.VisaListView.as_view(), name="visas"),
    path("services/", views.ServiceListView.as_view(), name="services"),
    path("visa/<str:slug>/", views.VisaDetailView.as_view(), name="visa_detail"),
    path("services/<str:slug>/", views.ServiceDetailView.as_view(), name="service_detail"),
]
