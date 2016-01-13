import reversion
from cms.apps.pages.admin import page_admin
from django.contrib import admin
from django.core.cache import cache
from suit.admin import SortableTabularInline

from compleat.apps.people.models import People
from compleat.apps.site.models import ContentSection, Content, FeatureCarousel, \
    FeatureCarouselSlide, FeatureCard, FeatureCards, BenefitCarouselSlide, \
    BenefitCarousel, Card, CardSet, FeaturePrimary, \
    FeatureSecondary, Feature, ExtraFeature, FooterColumn, FooterLink, FooterTip, \
    FeaturePageCardSet, FeaturePageCard, Sidebox, Sideboxes, LogoSet, Logo, \
    Link, LinkGroup


class ContentSectionInline(admin.StackedInline):
    model = ContentSection
    extra = 1
    filter_horizontal = ('people',)

    class Media:
        js = ('/static/js/admin/content-sections.js',)


class FeatureCarouselInline(admin.StackedInline):
    model = FeatureCarouselSlide
    extra = 1


@admin.register(FeatureCarousel)
class FeatureCarouselAdmin(reversion.VersionAdmin):
    inlines = [FeatureCarouselInline]


class FeatureCardInline(admin.StackedInline):
    model = FeatureCard
    extra = 1


@admin.register(FeatureCards)
class FeatureCardsAdmin(admin.ModelAdmin):
    inlines = [FeatureCardInline]


class BenefitCarouselInline(admin.StackedInline):
    model = BenefitCarouselSlide
    extra = 1


@admin.register(BenefitCarousel)
class BenefitCarouselAdmin(reversion.VersionAdmin):
    inlines = [BenefitCarouselInline]


class CardSetInline(admin.StackedInline):
    model = Card
    extra = 1


@admin.register(CardSet)
class CardSetAdmin(reversion.VersionAdmin):
    inlines = [CardSetInline]


class FeaturePageCardInline(admin.StackedInline):
    model = FeaturePageCard
    extra = 1


@admin.register(FeaturePageCardSet)
class FeaturePageCardSetAdmin(reversion.VersionAdmin):
    inlines = [FeaturePageCardInline]


class FeaturePrimaryInline(admin.StackedInline):
    model = FeaturePrimary
    extra = 1
    verbose_name = "Primary feature"
    verbose_name_plural = "Primary features"


class FeatureSecondaryInline(admin.StackedInline):
    model = FeatureSecondary
    extra = 1
    verbose_name = "Secondary feature"
    verbose_name_plural = "Secondary features"


class ExtraFeatureInline(admin.StackedInline):
    model = ExtraFeature
    extra = 3
    max_num = 3
    verbose_name = "Extra feature"
    verbose_name_plural = "Extra features"


class FooterLinkInline(admin.StackedInline):
    model = FooterLink
    extra = 1


@admin.register(FooterColumn)
class FooterColumnAdmin(admin.ModelAdmin):
    inlines = [FooterLinkInline]

    def save_model(self, request, obj, form, change):
        cache.delete('footer-columns')
        super(FooterColumnAdmin, self).save_model(request, obj, form, change)


@admin.register(FooterTip)
class FooterTipAdmin(admin.ModelAdmin):
    list_display = ["tip", "prefix", "link_text", "link_url"]

    def save_model(self, request, obj, form, change):
        cache.delete('footer-tips')
        super(FooterTipAdmin, self).save_model(request, obj, form, change)


class SideboxInline(admin.StackedInline):
    class Media:
        js = ("/static/js/admin_sideboxes.js", )
    model = Sidebox


@admin.register(Sideboxes)
class SideboxesAdmin(admin.ModelAdmin):
    inlines = (SideboxInline, )
    list_display = ("name", "sidebox_count", )

    class Media:
        js = ('/static/js/admin/sideboxes.js',)

    def sidebox_count(self, obj):
        return obj.sideboxes.count()


class LogoInline(admin.StackedInline):
    model = Logo
    extra = 1


@admin.register(LogoSet)
class LogoSetAdmin(reversion.VersionAdmin):
    inlines = [LogoInline]


class LinkInlineAdmin(SortableTabularInline):
    model = Link
    sortable = 'ordering'


@admin.register(LinkGroup)
class LinkGroupAdmin(reversion.VersionAdmin):
    inlines = [LinkInlineAdmin]

page_admin.register_content_inline(Content, ContentSectionInline)
page_admin.register_content_inline(People, ContentSectionInline)
page_admin.register_content_inline(Feature, FeaturePrimaryInline)
page_admin.register_content_inline(Feature, FeatureSecondaryInline)
page_admin.register_content_inline(Feature, ExtraFeatureInline)
