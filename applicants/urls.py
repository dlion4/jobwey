from django.urls import path
from . import views


app_name = "applicant"

urlpatterns = [
    path("", views.CandidatesListView.as_view(), name="applicant"),
    path("<applicant_public_profile_pk>/", views.PublicCandidateProfileView.as_view(), name="applicant_public_profile"),
    path("<str:company_slug>/<str:job_slug>/application", 
         views.ApplicationCreateView.as_view(), 
         name="application"
         ),
]

