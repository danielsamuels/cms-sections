from django.conf.urls import url
from django.contrib import admin

from .apps.site.models import sections_js

admin.autodiscover()


urlpatterns = [
    # Admin URLs.
    url(r'^admin/pages/page/sections.js$', sections_js, name="admin_sections_js"),
]
