from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls", namespace="account")),
    path("administrator/", include("administrator.urls", namespace="administrator")),
    path("", include("jobwey.urls", namespace="jobwey")),
    path("companies/", include("companies.urls", namespace="company")),
    path("applicants/", include("applicants.urls", namespace="applicant")),


    # frameworks
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
