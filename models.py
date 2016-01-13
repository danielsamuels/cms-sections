from django.db import models

from cms.apps.media.models import ImageRefField
from cms.apps.pages.models import Page
from cms.models import HtmlField

from ..forms.models import Form
from ..people.models import Person


SECTION_TYPES = (
    ("homepage-hero", "Homepage hero"),
    ("landing-hero", "Landing hero"),
    ("dynamic-demonstration", "Dynamic demonstration"),
    ("feature-carousel", "Feature carousel"),
    ("feature-cards", "Feature cards"),
    ("feature-page-cards", "Feature page cards"),
    ("benefit-carousel", "Benefit carousel"),
    ("people", "People"),
    ("cards", "Cards"),
    ("dual-column", "Dual column"),
    ("quote", "Quote"),
    ("quote-with-image", "Quote with image"),
    ("raw-html", "Raw HTML"),
    ("text-left-image-right", "Text left, image right"),
    ("text-right-image-left", "Text right, image left"),
    ("content", "Content"),
    ("image", "Image"),
    ("keyline", "Keyline"),
    ("form", "Form"),
)


class SectionBase(models.Model):
    type = models.CharField(
        choices=SECTION_TYPES,
        max_length=100
    )

    feature_carousel = models.ForeignKey(
        "site.FeatureCarousel",
        blank=True,
        null=True,
        help_text="Feature carousel you would like to display"
    )

    feature_cards = models.ForeignKey(
        "site.FeatureCards",
        blank=True,
        null=True,
        help_text="Feature card set you would like to display"
    )

    benefit_carousel = models.ForeignKey(
        "site.BenefitCarousel",
        blank=True,
        null=True,
        help_text="Benefit carousel you would like to display"
    )

    cards = models.ForeignKey(
        "site.CardSet",
        blank=True,
        null=True,
        help_text="The card set you would like to display"
    )

    feature_page_cards = models.ForeignKey(
        "site.FeaturePageCardSet",
        blank=True,
        null=True,
        help_text="The card set you would like to display"
    )

    people = models.ManyToManyField(
        Person,
        blank=True,
    )

    background_color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=(
            ('#fff', 'White'),
            ('#f0fbfb', 'Light blue'),
            ('#f6f6f6', 'Light grey')
        ),
        default='#fff'
    )

    title = models.CharField(
        max_length=140,
        blank=True,
        null=True
    )

    text = models.TextField(
        blank=True,
        null=True
    )

    background_image = ImageRefField(
        blank=True,
        null=True
    )

    image = ImageRefField(
        blank=True,
        null=True
    )

    video = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    button_url = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    content = HtmlField(
        blank=True,
        null=True
    )

    content_left = HtmlField(
        "Left content",
        blank=True,
        null=True
    )

    content_right = HtmlField(
        "Right content",
        blank=True,
        null=True
    )

    vertical_alignment = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=[
            ("align-middle", "Middle"),
            ("align-top", "Top"),
        ],
        default="align-middle",
    )

    quote_logo = ImageRefField(
        blank=True,
        null=True,
        help_text="Logo that will appear above the quote"
    )

    quote = models.TextField(
        max_length=300,
        blank=True,
        null=True
    )

    quote_author = models.CharField(
        max_length=140,
        blank=True,
        null=True
    )

    quote_author_company = models.CharField(
        max_length=140,
        blank=True,
        null=True
    )

    html = models.TextField(
        "HTML",
        null=True,
        blank=True,
    )

    show_logos = models.BooleanField(
        default=False
    )

    logo_set = models.ForeignKey(
        'site.LogoSet',
        blank=True,
        null=True
    )

    logo_set_title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    form = models.ForeignKey(
        Form,
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Order which the section will be displayed"
    )

    class Meta:
        abstract = True
        ordering = ('order',)

    def __unicode__(self):
        sections = {k: v for (k, v) in SECTION_TYPES}

        return sections[self.type]

    @property
    def template(self):
        return 'section_{}.html'.format(
            self.type.replace('-', '_')
        )


class ContentSection(SectionBase):

    parent = models.ForeignKey(
        Page
    )
