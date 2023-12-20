from . import views
from django.urls import path


app_name = "posts"


urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<str:post_slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
