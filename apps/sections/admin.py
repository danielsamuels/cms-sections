from cms.apps.pages.admin import page_admin
from django.core.urlresolvers import reverse_lazy
from suit.admin import SortableStackedInline

from .forms import TypeWidget
from .models import Content, ContentSection


class ContentSectionInline(SortableStackedInline):
    model = ContentSection
    extra = 0
    filter_horizontal = ['people']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'type':
            kwargs['widget'] = TypeWidget

        return super(ContentSectionInline, self).formfield_for_dbfield(db_field, **kwargs)

    class Media(object):
        js = [reverse_lazy('admin_sections_js')]

        css = {
            'all': ['/static/css/admin-sections.css'],
        }


page_admin.register_content_inline(Content, ContentSectionInline)
