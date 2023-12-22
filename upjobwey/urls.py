from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import (
    posts_dict,jobs_dict
)
from django.contrib.sitemaps import GenericSitemap
from .views import RoboticView



urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls", namespace="account")),
    path("administrator/", include("administrator.urls", namespace="administrator")),
    path("", include("jobwey.urls", namespace="jobwey")),
    path("companies/", include("companies.urls", namespace="company")),
    path("applicants/", include("applicants.urls", namespace="applicant")),
    path("posts/", include("posts.urls", namespace="posts")),


    # frameworks
    path('tinymce/', include('tinymce.urls')),
    path('avatar/', include('avatar.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": {"jobs": GenericSitemap(jobs_dict, priority=0.6),
        "posts": GenericSitemap(posts_dict, priority=0.6)
        }},
    name="django.contrib.sitemaps.views.sitemap",
),
    path("robots.txt",RoboticView.as_view()),
    path("aboutus/",views.AboutUsView.as_view(),name='aboutus'),
    path("contract/",views.ContractView.as_view(),name='contract'),
    path("contactus/",views.ContactView.as_view(),name='contact'),
    path("privacy/",views.PrivacyView.as_view(),name='privacy'),
    path("terms/",views.TermsView.as_view(),name='terms')
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
