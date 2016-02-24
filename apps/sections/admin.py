from cms.apps.pages.admin import page_admin
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from .models import Content, ContentSection


class ContentSectionInline(admin.StackedInline):
    model = ContentSection
    extra = 1
    filter_horizontal = ('people',)

    class Media(object):
        js = [reverse_lazy('admin_sections_js')]

        css = {
            'all': ['/static/css/admin-sections.css'],
        }

page_admin.register_content_inline(Content, ContentSectionInline)
