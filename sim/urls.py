from django.urls import URLPattern, path

from . import views

urlpatterns = [
        path("example/", views.example, name="example"),
        path("sample_post/", views.sample_post, name="sample_post")
]
