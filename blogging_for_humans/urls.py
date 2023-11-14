"""
URLs for blogging_for_humans.
"""
from django.conf.urls import include, url
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from . import views

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'^aaa', TemplateView.as_view(template_name="blogging_for_humans/base.html")),
    url(r"", include("lms.urls")),
    url(r"^aaa", views.render_something_from_model),
    url(r"bbb", TemplateView.as_view(template_name="blogging_for_humans/base.html")),
]
