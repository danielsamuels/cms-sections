from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def section(context, page_section):
    context.update({'section': page_section})

    return render_to_string('site/sections/{}'.format(
        page_section.template
    ), context)


@register.simple_tag(takes_context=True)
def section_contains_image(context, section):
    if not section.content_left or not section.content_right:
        return ''

    if any('<img' in s for s in[section.content_left, section.content_right]):
        return 'has-media'

    return ''
