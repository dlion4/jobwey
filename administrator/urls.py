from django.urls import path
from . import views
app_name= "administrator"

urlpatterns = [
    path("company/create/", views.CreateCompanyView.as_view(), name="create"),
    path("company/<str:slug>/update/", views.UpdateCompanyView.as_view(), name="company-update"),
    path("<slug>/job/create/", views.CreateCompanyPositionView.as_view(), name="position-create"),
    path("<slug>/job/create/", views.CreateCompanyPositionView.as_view(), name="position-create"),
]
