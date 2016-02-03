from cms.apps.media.models import ImageRefField
from cms.apps.pages.models import ContentBase, Page
from cms.models import HtmlField
from django.db import models
from django.shortcuts import render_to_response

SECTION_TYPES = (
    ("homepage-hero", {
        "name": "Homepage hero",
        "fields": ['title', 'text', 'button_text', 'button_url'],
    }),
    ("landing-hero", {
        "name": "Landing hero",
        "fields": ['title', 'text', 'image', 'button_text', 'button_url'],
    }),
    ("dual-column", {
        "name": "Dual column",
        "fields": ['title', 'text', 'button_text', 'button_url'],
    }),
    ("form", {
        "name": "Form",
        "fields": [],
    }),
    ("keyline", {
        "name": "Keyline",
    })
)


def sections_js(request):
    return render_to_response('admin/pages/page/sections.js', {
        'types': SECTION_TYPES,
    }, content_type='application/javascript')


class SectionBase(models.Model):

    page = models.ForeignKey(
        Page,
    )

    type = models.CharField(
        choices=[(s[0], s[1]['name']) for s in SECTION_TYPES],
        max_length=100,
    )

    title = models.CharField(
        max_length=140,
        blank=True,
        null=True,
    )

    text = models.TextField(
        blank=True,
        null=True,
    )

    content = HtmlField(
        blank=True,
        null=True,
    )

    image = ImageRefField(
        blank=True,
        null=True,
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    button_url = models.CharField(
        "button URL",
        max_length=200,
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Order which the section will be displayed",
    )

    class Meta:
        abstract = True
        ordering = ('order',)

    def __unicode__(self):
        return dict(SECTION_TYPES)[self.type]['name']

    @property
    def template(self):
        return '{}.html'.format(
            self.type.replace('-', '_')
        )


class ContentSection(SectionBase):
    pass


class Content(ContentBase):
    pass
