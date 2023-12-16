from django.urls import path
from . import views

app_name = "company"

urlpatterns = [
    path("<str:slug>/", views.CompanyDetailView.as_view(), name="company_detail_view"),
    path("jobs/listing/", views.JobListView.as_view(), name="job_list_view"),
    path("employers/listing/", views.CompanyListView.as_view(), name="company_list_view"),
    path("<str:company_slug>/<str:job_slug>/", views.JobDetailView.as_view(), name="job_detail_view"),
]
